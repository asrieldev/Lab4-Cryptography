# Lab 4 Cryptography

This VS Code project contains the four exercises from the Cryptography Fundamentals lab: AES encryption, RSA encryption, SHA-256 hashing, and RSA digital signatures.

## Open and run in VS Code

Open this folder in VS Code. In its integrated terminal, activate the included environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run all four exercises and save the output logs:

```powershell
python .\run_all.py
```

Run an exercise on its own:

```powershell
python .\exercise1_aes\aes_demo.py
python .\exercise2_rsa\rsa_demo.py
python .\exercise3_sha256\sha256_demo.py
python .\exercise4_signatures\signature_demo.py
```

To rebuild the environment on another computer, use an installed Python version supported by `cryptography`:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The `venv` directory is local to this computer and excluded by `.gitignore`. Recreate it with the commands above if it is missing.

## Experiments and variations

- **AES-256-GCM:** encrypts and decrypts text and rejects a modified ciphertext.
- **AES key sizes:** runs AES-128-GCM and AES-256-GCM on the same sample to compare the key sizes and resulting ciphertext lengths.
- **AES modes:** runs AES-256-CBC with PKCS7 padding as a mode comparison. Bare CBC does not authenticate ciphertext; GCM is the recommended authenticated mode in this demonstration.
- **RSA key sizes:** runs OAEP round trips with 2048-bit and 3072-bit RSA keys and records ciphertext sizes.
- **SHA-256 input types:** hashes empty and changed text, arbitrary binary bytes, and the JPEG screenshot file.
- **RSA-PSS signatures:** signs and verifies a message, then rejects a modified message. Signing uses a separate RSA key pair from encryption.

The combined machine-readable results are saved to `screenshots/experiment_log.json`. Separate logs for each exercise are written beside it. The screenshot `screenshots/vscode_run.jpg` was captured before the project was moved into Documents, so its visible terminal path shows the earlier workspace location. The image is kept as captured. Keys stay in memory and are not saved to the logs.

## Project contents

- `exercise1_aes/`, `exercise2_rsa/`, `exercise3_sha256/`, `exercise4_signatures/`: standalone programs for each exercise.
- `screenshots/`: original VS Code run screenshot and combined/per-exercise JSON logs.
- `report/`: editable report and PDF copy.
- `run_all.py`: runs every exercise and records the results.

# Dear cryptographer:
# When I wrote this code, only God and I knew how it worked.
# Now only God knows!
# The AES key is random, the nonce is unique,
# and the ciphertext is authenticated.
# If decryption still fails, check the AAD
# before blaming quantum computing & debugging_hours_spent = 5