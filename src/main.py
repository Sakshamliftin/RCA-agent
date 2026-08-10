import os
import argparse
import sys

# Ensure the root of the project is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.parsers.exec_log_parser import ExecutionLogParser
from src.parsers.deep_xml_parser import DeepXMLParser
from src.rule_engine import RuleEngine
from src.llm_analyzer import LLMAnalyzer

os.environ["GEMINI_API_KEY"] = "AQ.Ab8RN6KVl1L-xvHCLsfCo8vNL9ZrLruUk4tAlz3b_AnILc-7Qw"

class LocalRCAPipeline:
    def __init__(self):
        self.llm = LLMAnalyzer()

    def analyze_directory(self, target_dir):
        result = {
            "directory": target_dir,
            "status": "success",
            "triage_rules": [],
            "llm_analysis": "",
            "slicer_hits": 0,
            "error": None
        }
        
        xml_path = os.path.join(target_dir, "output.xml")
        
        exec_errors = ExecutionLogParser.extract_critical_errors(target_dir)
        deep_failures = DeepXMLParser.find_lowest_level_failures(xml_path)
        
        if not deep_failures:
            result["error"] = "No leaf keyword failures found or XML missing."
            result["status"] = "skipped"
            return result

        # Evaluate only the first root cause failure to avoid teardown noise
        target_fail = deep_failures[0]
        combined_context = " ".join(exec_errors) + f" {target_fail['error_message']}"
            
        triage_results = RuleEngine.classify(combined_context)
        
        if triage_results:
            result["triage_rules"] = triage_results
        else:
            for target_fail in deep_failures:
                if target_fail.get('dependency_chain'):
                    result["slicer_hits"] = len(target_fail['dependency_chain'])
                    break
            
            analysis = self.llm.analyze(deep_failures, exec_errors)
            result["llm_analysis"] = analysis
            
        return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs="?", default="data", help="Path to logs")
    args = parser.parse_args()
    agent = LocalRCAPipeline()
    res = agent.analyze_directory(args.directory)
    if res["triage_rules"]:
        print(f"Rules Matched: {res['triage_rules']}")
    else:
        print(f"LLM Analysis:\n{res['llm_analysis']}")
