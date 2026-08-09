import urllib.request
import json
import os
import subprocess

def download_dataset():
    url = "http://10.35.0.214:8000/executions/test-execution-result/?page=1&page_size=20&ordering=-id&test_status=Fail"
    token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg2MDQ2Nzg3LCJpYXQiOjE3ODYwMzU5ODcsImp0aSI6ImM3MmQ5MGMwMzQxNTRmOTc5M2I5ZDUxZDA0YzIyMTdmIiwidXNlcl9pZCI6Ijg0In0.oNgCzDjx-LrvPXIzIlElxiRfmDLUzp36Ci-BgyF1hqs"

    print("Fetching top 20 test failures from AURA...")
    req = urllib.request.Request(url)
    req.add_header("Authorization", token)
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
    except Exception as e:
        print(f"Failed to query AURA API: {e}")
        return

    results = data.get('results', [])
    print(f"Got {len(results)} failed test executions. Starting download...")
    
    os.makedirs("poc_dataset", exist_ok=True)
    
    for r in results:
        ater_id = r.get('ater_id')
        log_path = r.get('log_path')
        if not ater_id or not log_path:
            continue
            
        target_dir = os.path.join("poc_dataset", ater_id)
        os.makedirs(target_dir, exist_ok=True)
        
        xml_url = f"{log_path}/output.xml"
        xml_dest = os.path.join(target_dir, "output.xml")
        
        if not os.path.exists(xml_dest):
            print(f"[{ater_id}] Downloading output.xml...")
            try:
                urllib.request.urlretrieve(xml_url, xml_dest)
            except urllib.error.HTTPError as e:
                print(f"[{ater_id}] output.xml not found on server ({e.code})")
            except Exception as e:
                print(f"[{ater_id}] Error downloading: {e}")
        else:
            print(f"[{ater_id}] output.xml already exists, skipping.")
            
    print("\nDownload complete! Running POC Agent over dataset...")
    
    # Run the POC agent on every directory
    for item in os.listdir("poc_dataset"):
        dir_path = os.path.join("poc_dataset", item)
        if os.path.isdir(dir_path):
            subprocess.run(["python", "poc_rca_agent.py", dir_path])

if __name__ == "__main__":
    download_dataset()
