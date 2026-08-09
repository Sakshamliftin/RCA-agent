import os
from google import genai

class LLMAnalyzer:
    def __init__(self):
        api_key = os.environ.get("GEMINI_API_KEY")
        if api_key:
            self.client = genai.Client(api_key=api_key)
        else:
            self.client = None
            
        self.knowledge_base = ""
        kb_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "knowledge_base.md")
        if os.path.exists(kb_path):
            with open(kb_path, "r", encoding="utf-8") as f:
                self.knowledge_base = f.read()
            
    def analyze(self, failures, exec_errors):
        if not self.client:
            return "[API Key missing - LLM skipped]"
            
        prompt = "You are an expert test automation engineer diagnosing a Robot Framework failure.\n\n"
        
        if self.knowledge_base:
            prompt += "--- DOMAIN KNOWLEDGE & UNWRITTEN RULES ---\n"
            prompt += "Apply these rules strictly when diagnosing the root cause. If a failure can be explained by a known quirk below, highlight it!\n"
            prompt += self.knowledge_base + "\n\n"
        
        if exec_errors:
            prompt += "BACKGROUND INFRASTRUCTURE ERRORS (may be related):\n"
            for err in exec_errors:
                prompt += f"- {err}\n"
            prompt += "\n"
            
        prompt += "Below is the chronological sequence of all failing keywords in this test execution.\n"
        prompt += "Some may be non-fatal assertions (e.g., 'Dictionary does not contain key'), and some may be teardown noise (e.g., 'Browser not started', 'TypeError: Popen').\n"
        prompt += "Your job is to identify the PRIMARY FATAL CRASH that ruined the test logic, and explain its root cause.\n\n"
        
        for idx, failure in enumerate(failures):
            prompt += f"--- FAILURE {idx + 1} ---\n"
            prompt += f"CRASHING KEYWORD: {failure['failing_keyword']}\n"
            if failure.get("intent"):
                prompt += f"KEYWORD INTENT: {failure['intent']}\n"
            prompt += f"EXACT ERROR: {failure['error_message']}\n"
            if failure.get("traceback"):
                prompt += f"TRACEBACK: {failure['traceback']}\n"
            
            if failure.get("context_logs"):
                prompt += f"CONTEXTUAL LOGS (Leading up to this failure):\n"
                for log in failure["context_logs"]:
                    prompt += f"  {log}\n"
            
            if failure.get('target_vars'):
                prompt += f"FAULTY VARIABLES DETECTED: {', '.join(failure['target_vars'])}\n"
        
            if failure.get('dependency_chain'):
                prompt += "DATA FLOW TAINT TRACKING:\n"
                for link in failure['dependency_chain']:
                    prompt += f"  [Depth {link['depth']}] Variable '{link['variable']}' was assigned by: {link['assigning_keyword']}\n"
                    if link.get("assigning_intent"):
                        prompt += f"    INTENT: {link['assigning_intent']}\n"
            prompt += "\n"
            
        prompt += "TASK:\n1. Ignore teardown noise and non-fatal warnings.\n2. Identify the true root cause failure (which might be hidden in the contextual INFO logs of a generic 'Fail' keyword).\n3. Compare the keyword's intent to its actual outcome.\n4. Explain the ultimate root cause in 2 or 3 concise sentences."
        
        try:
            response = self.client.models.generate_content(
                model='gemini-3.5-flash',
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"LLM Invocation Failed: {e}"
