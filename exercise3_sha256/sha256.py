"""Exercise 3: SHA-256 for text, binary bytes, and an image file."""

import hashlib
import json
from pathlib import Path


def run() -> dict:
    sample = b"Cryptography protects information."
    changed = b"cryptography protects information."
    empty_digest = hashlib.sha256(b"").hexdigest()
    sample_digest = hashlib.sha256(sample).hexdigest()
    changed_digest = hashlib.sha256(changed).hexdigest()
    differing_bits = (int(sample_digest, 16) ^ int(changed_digest, 16)).bit_count()

    binary_sample = bytes([0, 1, 2, 128, 255])
    binary_digest = hashlib.sha256(binary_sample).hexdigest()
    image_path = Path(__file__).resolve().parents[1] / "screenshots" / "vscode_run.jpg"
    image_bytes = image_path.read_bytes() if image_path.is_file() else b""
    image_digest = hashlib.sha256(image_bytes).hexdigest() if image_bytes else None

    checks = {
        "digest_is_256_bits": len(bytes.fromhex(sample_digest)) * 8 == 256,
        "changed_input_changes_digest": sample_digest != changed_digest,
        "binary_input_hashed": len(bytes.fromhex(binary_digest)) == 32,
        "image_input_hashed": image_digest is not None,
    }
    return {
        "algorithm": "SHA-256",
        "empty_input_digest": empty_digest,
        "sample_input": sample.decode("utf-8"),
        "sample_digest": sample_digest,
        "one_character_changed_input": changed.decode("utf-8"),
        "changed_digest": changed_digest,
        "changed_digest_bits_different": differing_bits,
        "changed_digest_bits_total": 256,
        "binary_sample_hex": binary_sample.hex(),
        "binary_sample_digest": binary_digest,
        "image_file": "screenshots/vscode_run.jpg",
        "image_bytes": len(image_bytes),
        "image_sha256": image_digest,
        "checks": checks,
        "passed": all(checks.values()),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
