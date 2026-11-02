# Lab 4 evidence inventory

**Project:** `C:\Users\MrRobot\Documents\Lab4-Cryptography`  
**Combined run timestamp (UTC):** `2026-11-02T15:22:57.274592+00:00`  
**Runtime:** Python 3.12.14; `cryptography` 50.0.2  
**Combined result:** `passed: true`; all four exercise logs report `passed: true`.

## Evidence available

| Evidence | Location | Status and interpretation |
|---|---|---|
| Combined terminal output | `screenshots/experiment_output.txt` | Captures output from `run_all.py`; paired with the combined JSON log. |
| Combined structured results | `screenshots/experiment_log.json` | Current run at the timestamp above; includes per-exercise checks and measured values. |
| AES detail log | `screenshots/aes_log.json` | Current combined run. |
| RSA-OAEP detail log | `screenshots/rsa_encryption_log.json` | Current combined run. |
| SHA-256 detail log | `screenshots/sha256_log.json` | Current combined run, including text, binary, and JPEG input checks. |
| RSA-PSS signature detail log | `screenshots/digital_signature_log.json` | Current combined run. |
| AES terminal screenshot and matching standalone log | `screenshots/aes_terminal_execution.jpg`, `screenshots/aes_execution.json` | Available and genuine. This standalone run has random values that differ from the combined run; the two records should not be treated as one execution. |
| Earlier all-exercise screenshot | `screenshots/vscode_run.jpg` | Preserved historical evidence from before the project folder move. The earlier workspace path is visible. It was not used to support current measured values. |
| Additional AES terminal screenshot | `screenshots/combined_run.jpg` | Genuine screenshot of a separate AES exercise run in the Documents project folder. It is now included in the report as a second AES capture; its values are not used for the combined-run results. |

The combined JSON results state that key material was not logged. The report does not claim that the experiment validates production key management or deployment security.

## Remaining screenshot gaps

Dedicated terminal screenshots for RSA-OAEP, SHA-256, and RSA-PSS are not present. The corresponding current JSON logs and combined terminal output are available; the supplied lab brief accepts screenshots **or logs**. If separate screenshots are desired, run these commands from the project root in the VS Code terminal, capture the actual output without editing it, and save the images in `screenshots/`:

```powershell
python .\exercise2_rsa\rsa_demo.py
python .\exercise3_sha256\sha256_demo.py
python .\exercise4_signatures\signature_demo.py
```

## Reproduce the complete experiment

From the project root, activate the virtual environment and run all exercises:

```powershell
.\venv\Scripts\Activate.ps1
python .\run_all.py
```

To run an individual script, use Python explicitly (PowerShell does not automatically execute a script from the current directory by its bare filename):

```powershell
python .\exercise1_aes\aes_demo.py
python .\exercise2_rsa\rsa_demo.py
python .\exercise3_sha256\sha256_demo.py
python .\exercise4_signatures\signature_demo.py
```

In the AES exercise folder, the equivalent command is `python .\aes_demo.py`. Typing `aes_demo.py` alone produces the PowerShell “not recognized” error shown in the user's terminal; `.\aes_demo.py` is a PowerShell path form, but invoking it through Python is consistent and avoids reliance on file associations.

## Code-to-evidence map

| Exercise | Source | Combined result file |
|---|---|---|
| AES-256-GCM and CBC comparison | `exercise1_aes/aes_demo.py` | `screenshots/aes_log.json` |
| RSA-OAEP | `exercise2_rsa/rsa_demo.py` | `screenshots/rsa_encryption_log.json` |
| SHA-256 | `exercise3_sha256/sha256_demo.py` | `screenshots/sha256_log.json` |
| RSA-PSS digital signature | `exercise4_signatures/signature_demo.py` | `screenshots/digital_signature_log.json` |


