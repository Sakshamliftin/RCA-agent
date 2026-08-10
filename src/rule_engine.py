import re

class RuleEngine:
    RULES = [
        (re.compile(r"github authentication|permission denied \(publickey\)", re.I), "Jenkins: GitHub Auth Failure"),
        (re.compile(r"Authentication failed|SSH connection could not be established", re.I), "Infrastructure: SSH Key/Auth Failure to Node or UE Helper"),
        (re.compile(r"Timeout \d+ms exceeded|locator", re.I), "UI/Test: Dashboard Locator Timeout"),
        # (re.compile(r"Expected argument 1 to be a dictionary, got Popen", re.I), "Test Script Maintenance: Subprocess object passed instead of Dictionary")
    ]
    
    @staticmethod
    def classify(error_text):
        matches = []
        for pattern, classification in RuleEngine.RULES:
            if pattern.search(error_text):
                matches.append(classification)
        return matches
