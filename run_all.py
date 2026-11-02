"""Run all four cryptography lab exercises and save evidence logs."""

import json
import platform
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path

from exercise1_aes.aes_demo import run as run_aes
from exercise2_rsa.rsa_demo import run as run_rsa
from exercise3_sha256.sha256_demo import run as run_sha256
from exercise4_signatures.signature_demo import run as run_signature


def main() -> int:
    results = {
        "lab": "Cryptography Fundamentals Lab 4",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {
            "python": platform.python_version(),
            "cryptography": version("cryptography"),
        },
        "exercises": {
            "aes": run_aes(),
            "rsa_encryption": run_rsa(),
            "sha256": run_sha256(),
            "digital_signature": run_signature(),
        },
    }
    results["passed"] = all(item["passed"] for item in results["exercises"].values())
    rendered = json.dumps(results, indent=2, sort_keys=True) + "\n"

    evidence_dir = Path(__file__).resolve().parent / "screenshots"
    evidence_dir.mkdir(exist_ok=True)
    (evidence_dir / "experiment_log.json").write_text(rendered, encoding="utf-8")
    for name, experiment in results["exercises"].items():
        per_exercise = {
            "lab": results["lab"],
            "timestamp_utc": results["timestamp_utc"],
            "runtime": results["runtime"],
            "exercise": name,
            "result": experiment,
        }
        filename = f"{name}_log.json"
        (evidence_dir / filename).write_text(
            json.dumps(per_exercise, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    print(rendered, end="")
    print(f"Evidence log saved to: {evidence_dir / 'experiment_log.json'}")
    return 0 if results["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
