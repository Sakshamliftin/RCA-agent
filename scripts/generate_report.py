import os
import sys
import glob
import time

# Ensure the root of the project is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import LocalRCAPipeline

def generate_report():
    dataset_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "poc_dataset")
    dirs = [d for d in glob.glob(os.path.join(dataset_dir, "*")) if os.path.isdir(d)]
    
    agent = LocalRCAPipeline()
    results = []
    
    print(f"Found {len(dirs)} executions. Starting batch processing...")
    
    for idx, d in enumerate(dirs):
        folder_name = os.path.basename(d)
        print(f"Processing {idx+1}/{len(dirs)}: {folder_name}...")
        try:
            res = agent.analyze_directory(d)
            results.append(res)
            # Sleep briefly to avoid aggressive rate limiting on Gemini API
            if not res.get("triage_rules") and res.get("status") != "skipped":
                time.sleep(4) 
        except Exception as e:
            results.append({
                "directory": folder_name,
                "status": "error",
                "error": str(e)
            })
            
    # Write Markdown Report
    report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "RCA_Performance_Report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# RCA Agent Performance Report\n\n")
        f.write("This report summarizes the triage results of the RCA Agent across the entire POC dataset.\n\n")
        
        f.write("## Executive Summary\n\n")
        f.write("| Execution ID | Triage Engine | Root Cause / Rule Matched |\n")
        f.write("|--------------|---------------|---------------------------|\n")
        
        for r in results:
            ater_id = os.path.basename(r['directory'])
            if r.get("status") == "skipped" or r.get("status") == "error":
                f.write(f"| {ater_id} | Skipped/Error | {r.get('error')} |\n")
            elif r.get("triage_rules"):
                rules = "<br>".join(r["triage_rules"])
                f.write(f"| {ater_id} | 🤖 Rule Engine | {rules} |\n")
            else:
                summary = "LLM Analysis (See Deep Dive below)"
                if "LLM Invocation Failed" in r.get("llm_analysis", ""):
                    summary = "LLM Failed (503/Rate Limit)"
                f.write(f"| {ater_id} | 🧠 LLM Detective | {summary} (Slicer Hits: {r.get('slicer_hits', 0)}) |\n")
                
        f.write("\n\n## LLM Detective Deep Dives\n\n")
        
        for r in results:
            if not r.get("triage_rules") and r.get("status") == "success":
                ater_id = os.path.basename(r['directory'])
                f.write(f"### {ater_id}\n")
                f.write(f"**Data Flow Slicer Hits:** {r.get('slicer_hits', 0)} levels deep\n\n")
                f.write(f"**LLM Diagnosis:**\n")
                f.write(f"> {r.get('llm_analysis').replace(chr(10), chr(10)+'> ')}\n\n")
                f.write("---\n\n")
                
    print(f"\nReport generated successfully: {report_path}")

if __name__ == "__main__":
    generate_report()
