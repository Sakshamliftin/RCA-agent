# POC RCA Analysis Results

Here are the detailed outputs from running our `poc_rca_agent.py` over the 6 test failures we successfully downloaded from AURA.

```text

============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27206
============================================================
[PHASE 1] Scanning execution_log/ for infrastructure drops...
  -> No infrastructure errors found in execution log.

[PHASE 2] Parsing output.xml for lowest-level Robot failure...
  -> Bypassed AURA surface error. Found 6 root cause failure(s).

     [Failure 1]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'LTE'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 2]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'WSCMN'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 3]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'PLAT'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 4]
     Failing Keyword : Run Process
     Exact Error     : Variable '${pcap_file}' not found.

     [Failure 5]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : TypeError: Expected argument 1 to be a dictionary, got Popen instead.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 6]
     Failing Keyword : Close Browser
     Exact Error     : Browser not started. Please call keyword: Start Browser
     Source File     : /home/jenkins/workspace/AIVergeExecution-Victor_10.240.112.98/venv/lib/python3.12/site-packages/AIVergeInfra/VSNET_GUI/robotlib/keywords.py (Line 302)

[PHASE 3] Running Deterministic Rule Engine...

************************************************************
FINAL RCA CLASSIFICATION(S) FOUND:
  -> Test Script Maintenance: Subprocess object passed instead of Dictionary (High Confidence)

   Action: Auto-matched by Rule Engine. Bypassing LLM API.
************************************************************


================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27208
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27210
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27211
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27213
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27215
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27216
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27219
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27225
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27226
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27228
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27231
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27233
============================================================
[PHASE 1] output.xml MISSING! The Robot test framework did not execute.
          Diagnosis: This is a Pipeline/Jenkins setup failure.

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27235
============================================================
[PHASE 1] Scanning execution_log/ for infrastructure drops...
  -> No infrastructure errors found in execution log.

[PHASE 2] Parsing output.xml for lowest-level Robot failure...
  -> Bypassed AURA surface error. Found 1 root cause failure(s).

     [Failure 1]
     Failing Keyword : N/A
     Exact Error     : XML Parse Error - output.xml is corrupted

================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27236
============================================================
[PHASE 1] Scanning execution_log/ for infrastructure drops...
  -> No infrastructure errors found in execution log.

[PHASE 2] Parsing output.xml for lowest-level Robot failure...
  -> Bypassed AURA surface error. Found 6 root cause failure(s).

     [Failure 1]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key '5GNR'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 2]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'WSCMN'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 3]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'PLAT'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 4]
     Failing Keyword : Fail
     Exact Error     : Failed to detach UEs: ['UE2_velocity']
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 5]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : TypeError: Expected argument 1 to be a dictionary, got Popen instead.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 6]
     Failing Keyword : Close Browser
     Exact Error     : Browser not started. Please call keyword: Start Browser
     Source File     : /home/jenkins/workspace/AIVergeExecution-ME1200_Velocity/venv/lib/python3.12/site-packages/AIVergeInfra/VSNET_GUI/robotlib/keywords.py (Line 302)

[PHASE 3] Running Deterministic Rule Engine...

************************************************************
FINAL RCA CLASSIFICATION(S) FOUND:
  -> UE Helper: Modem Lockup / Detach Failure (High Confidence)
  -> Test Script Maintenance: Subprocess object passed instead of Dictionary (High Confidence)

   Action: Auto-matched by Rule Engine. Bypassing LLM API.
************************************************************


================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27238
============================================================
[PHASE 1] Scanning execution_log/ for infrastructure drops...
  -> No infrastructure errors found in execution log.

[PHASE 2] Parsing output.xml for lowest-level Robot failure...
  -> Bypassed AURA surface error. Found 8 root cause failure(s).

     [Failure 1]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key '5GNR'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 2]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'LTE'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 3]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'WSCMN'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 4]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'PLAT'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 5]
     Failing Keyword : Get From Dictionary
     Exact Error     : Dictionary does not contain key '1'.

     [Failure 6]
     Failing Keyword : Fail
     Exact Error     : Failed to get IPs for UEs: ['UE_Fortuner_n261']
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 7]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : TypeError: Expected argument 1 to be a dictionary, got Popen instead.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 8]
     Failing Keyword : Close Browser
     Exact Error     : Browser not started. Please call keyword: Start Browser
     Source File     : /home/jenkins/workspace/AIVergeDev-ME-2K_Fortuner_LTE/venv/lib/python3.12/site-packages/AIVergeInfra/VSNET_GUI/robotlib/keywords.py (Line 302)

[PHASE 3] Running Deterministic Rule Engine...

************************************************************
FINAL RCA CLASSIFICATION(S) FOUND:
  -> Test Script Maintenance: Subprocess object passed instead of Dictionary (High Confidence)

   Action: Auto-matched by Rule Engine. Bypassing LLM API.
************************************************************


================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27241
============================================================
[PHASE 1] Scanning execution_log/ for infrastructure drops...
  -> No infrastructure errors found in execution log.

[PHASE 2] Parsing output.xml for lowest-level Robot failure...
  -> Bypassed AURA surface error. Found 8 root cause failure(s).

     [Failure 1]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'LTE'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 2]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'WSCMN'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 3]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key '5GNR'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 4]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'PLAT'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 5]
     Failing Keyword : Get From Dictionary
     Exact Error     : Dictionary does not contain key '1'.

     [Failure 6]
     Failing Keyword : Fail
     Exact Error     : Failed to get IPs for UEs: ['UE_Fortuner_n261']
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 7]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : TypeError: Expected argument 1 to be a dictionary, got Popen instead.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 8]
     Failing Keyword : Close Browser
     Exact Error     : Browser not started. Please call keyword: Start Browser
     Source File     : /home/jenkins/workspace/AIVergeDev-ME-2K_Fortuner_LTE/venv/lib/python3.12/site-packages/AIVergeInfra/VSNET_GUI/robotlib/keywords.py (Line 302)

[PHASE 3] Running Deterministic Rule Engine...

************************************************************
FINAL RCA CLASSIFICATION(S) FOUND:
  -> Test Script Maintenance: Subprocess object passed instead of Dictionary (High Confidence)

   Action: Auto-matched by Rule Engine. Bypassing LLM API.
************************************************************


================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27245
============================================================
[PHASE 1] Scanning execution_log/ for infrastructure drops...
  -> No infrastructure errors found in execution log.

[PHASE 2] Parsing output.xml for lowest-level Robot failure...
  -> Bypassed AURA surface error. Found 12 root cause failure(s).

     [Failure 1]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'LTE'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 2]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'WSCMN'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 3]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key '5GNR'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 4]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'PLAT'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 5]
     Failing Keyword : Get From Dictionary
     Exact Error     : Dictionary does not contain key '1'.

     [Failure 6]
     Failing Keyword : Fail
     Exact Error     : RCP-0 did not recover after reboot
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 7]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : TypeError: Expected argument 1 to be a dictionary, got Popen instead.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 8]
     Failing Keyword : Split To Lines
     Exact Error     : AttributeError: 'NoneType' object has no attribute 'splitlines'
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 9]
     Failing Keyword : Split To Lines
     Exact Error     : AttributeError: 'NoneType' object has no attribute 'splitlines'
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 10]
     Failing Keyword : Get From Dictionary
     Exact Error     : Dictionary does not contain key 'filename'.

     [Failure 11]
     Failing Keyword : Compare Json Files Infra
     Exact Error     : FileNotFoundError: Second file: None not found
     Source File     : /home/jenkins/workspace/AIVergeDev-ME-2K_Fortuner_LTE/venv/lib/python3.12/site-packages/AIVergeInfra/General/Helpers.py (Line 305)

     [Failure 12]
     Failing Keyword : Close Browser
     Exact Error     : Browser not started. Please call keyword: Start Browser
     Source File     : /home/jenkins/workspace/AIVergeDev-ME-2K_Fortuner_LTE/venv/lib/python3.12/site-packages/AIVergeInfra/VSNET_GUI/robotlib/keywords.py (Line 302)

[PHASE 3] Running Deterministic Rule Engine...

************************************************************
FINAL RCA CLASSIFICATION(S) FOUND:
  -> Test Script Maintenance: Subprocess object passed instead of Dictionary (High Confidence)

   Action: Auto-matched by Rule Engine. Bypassing LLM API.
************************************************************


================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27248
============================================================
[PHASE 1] Scanning execution_log/ for infrastructure drops...
  -> No infrastructure errors found in execution log.

[PHASE 2] Parsing output.xml for lowest-level Robot failure...
  -> Bypassed AURA surface error. Found 11 root cause failure(s).

     [Failure 1]
     Failing Keyword : Fail
     Exact Error     : CLI Command 'show Version Detail' failed for RCP 0
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 2]
     Failing Keyword : SCP From Remote
     Exact Error     : Variable '${remote_host}' not found.

     [Failure 3]
     Failing Keyword : Directory Should Exist
     Exact Error     : Directory '/home/jenkins/workspace/AIVergeDev-ME-2K_Fortuner_LTE/results/ME-2K_Fortuner_LTE/2026_08_05_23_27_57/ATC-549-1/debug_logs' does not exist.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 4]
     Failing Keyword : Split To Lines
     Exact Error     : AttributeError: 'NoneType' object has no attribute 'splitlines'
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 5]
     Failing Keyword : Split To Lines
     Exact Error     : AttributeError: 'NoneType' object has no attribute 'splitlines'
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 6]
     Failing Keyword : Evaluate
     Exact Error     : Evaluating expression 'list(set($Final_error_list) - set($Initial_error_list))' failed: Variable '$Initial_error_list' not found. Did you mean:
    $Final_error_list

     [Failure 7]
     Failing Keyword : Create Remote Directory
     Exact Error     : Variable '${remote_host}' not found.

     [Failure 8]
     Failing Keyword : Set Variable If
     Exact Error     : Variable '${cmd}' not found. Did you mean:
    ${cmd_list}

     [Failure 9]
     Failing Keyword : Get From Dictionary
     Exact Error     : Dictionary does not contain key 'filename'.

     [Failure 10]
     Failing Keyword : Compare JSON Files
     Exact Error     : Variable '${Initial_Alarm_event_json_file}' not found. Did you mean:
    ${Final_Alarm_event_json_file}

     [Failure 11]
     Failing Keyword : Close Browser
     Exact Error     : Browser not started. Please call keyword: Start Browser
     Source File     : /home/jenkins/workspace/AIVergeDev-ME-2K_Fortuner_LTE/venv/lib/python3.12/site-packages/AIVergeInfra/VSNET_GUI/robotlib/keywords.py (Line 302)

[PHASE 3] Running Deterministic Rule Engine...

************************************************************
FINAL RCA CLASSIFICATION: Unknown / Novel Failure
   Action: In production, this context will be sent to the RAG/LLM Planning Agent for deep diagnosis.

   [LLM Prompt Payload Preview]
   Keyword: Fail
   Error: CLI Command 'show Version Detail' failed for RCP 0
************************************************************


================================================================================


============================================================
AI RCA Agent (POC) - Analyzing Directory: poc_dataset\ATER-27253
============================================================
[PHASE 1] Scanning execution_log/ for infrastructure drops...
  -> No infrastructure errors found in execution log.

[PHASE 2] Parsing output.xml for lowest-level Robot failure...
  -> Bypassed AURA surface error. Found 12 root cause failure(s).

     [Failure 1]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key '5GNR'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 2]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'LTE'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 3]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'WSCMN'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 4]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : Dictionary does not contain key 'PLAT'.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 5]
     Failing Keyword : Get From Dictionary
     Exact Error     : Dictionary does not contain key '1'.

     [Failure 6]
     Failing Keyword : Fail
     Exact Error     : RCP-0 did not recover after reboot
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 7]
     Failing Keyword : Dictionary Should Contain Key
     Exact Error     : TypeError: Expected argument 1 to be a dictionary, got Popen instead.
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 8]
     Failing Keyword : Split To Lines
     Exact Error     : AttributeError: 'NoneType' object has no attribute 'splitlines'
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 9]
     Failing Keyword : Split To Lines
     Exact Error     : AttributeError: 'NoneType' object has no attribute 'splitlines'
     Source File     : [Line number suppressed by Robot Framework]

     [Failure 10]
     Failing Keyword : Get From Dictionary
     Exact Error     : Dictionary does not contain key 'filename'.

     [Failure 11]
     Failing Keyword : Compare Json Files Infra
     Exact Error     : FileNotFoundError: Second file: None not found
     Source File     : /home/jenkins/workspace/AIVergeDev-ME-2K_Fortuner_LTE/venv/lib/python3.12/site-packages/AIVergeInfra/General/Helpers.py (Line 305)

     [Failure 12]
     Failing Keyword : Close Browser
     Exact Error     : Browser not started. Please call keyword: Start Browser
     Source File     : /home/jenkins/workspace/AIVergeDev-ME-2K_Fortuner_LTE/venv/lib/python3.12/site-packages/AIVergeInfra/VSNET_GUI/robotlib/keywords.py (Line 302)

[PHASE 3] Running Deterministic Rule Engine...

************************************************************
FINAL RCA CLASSIFICATION(S) FOUND:
  -> Test Script Maintenance: Subprocess object passed instead of Dictionary (High Confidence)

   Action: Auto-matched by Rule Engine. Bypassing LLM API.
************************************************************


================================================================================

```
