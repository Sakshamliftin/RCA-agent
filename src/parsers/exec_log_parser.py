import os
import glob

class ExecutionLogParser:
    @staticmethod
    def extract_critical_errors(log_dir):
        exec_log_dir = os.path.join(log_dir, "execution_log")
        if not os.path.exists(exec_log_dir):
            return []
        errors_found = []
        for log_file in glob.glob(os.path.join(exec_log_dir, "*.txt")):
            with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
                for line in reversed(lines):
                    if "ERROR" in line or "Exception" in line or "Traceback" in line:
                        clean_line = line.strip()
                        if clean_line and "urllib3.connectionpool" not in clean_line:
                            errors_found.append(clean_line)
                    if len(errors_found) >= 3:
                        break
        return errors_found
