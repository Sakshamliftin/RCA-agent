import os
import subprocess

artifact_path = r"C:\Users\ssaklani\.gemini\antigravity-ide\brain\53cfa634-2ab5-4a7d-aecd-619adee2696d\analysis_results.md"

with open(artifact_path, "w", encoding="utf-8") as f:
    f.write("# POC RCA Analysis Results\n\n")
    f.write("Here are the detailed outputs from running our `poc_rca_agent.py` over the 6 test failures we successfully downloaded from AURA.\n\n")
    f.write("```text\n")
    
    dataset_dir = "poc_dataset"
    for item in os.listdir(dataset_dir):
        path = os.path.join(dataset_dir, item)
        if os.path.isdir(path):
            result = subprocess.run(["python", "poc_rca_agent.py", path], capture_output=True, text=True, encoding="utf-8", errors="replace")
            f.write(result.stdout)
            f.write("\n" + "="*80 + "\n\n")
            
    f.write("```\n")

print(f"Results saved to artifact: {artifact_path}")
