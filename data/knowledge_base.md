# RCA Agent Domain Knowledge Base

The LLM should strictly apply these unwritten rules and domain logic when diagnosing test failures.

- **SW Upgrades & Version Matching**: Installed software versions often append a 7-digit build number (e.g., `26.2.6.60.6137254`). When comparing installed vs target versions, you must mentally strip the build number. If the base versions match (e.g. `26.2.6.60`), it is a match. If a script fails to strip this and crashes, the root cause is a test script bug (missing string trim).
- **Import Errors**: Import errors may sometimes occur but still allow the rest of the script to continue. Only look at the final fatal errors that actually aborted the test logic. Ignore import errors unless they are the direct and only cause of the fatal crash.
- **Node Connectivity (Offline Nodes)**: If the test crashes because a node went offline and didn't come back up (e.g., SSH disconnected, unreachable, ping failed), this is likely a genuine PRODUCT ISSUE and must be flagged that way, rather than a test script error.
- **BOM Downloads**: SCP failures for `pkg.bom` may sometimes occur. Ensure you verify if this is the true root cause, or if there is a more explicit product/script failure later in the logs.
