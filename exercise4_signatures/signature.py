"""Exercise 4: RSA-PSS signing, verification, and changed-message rejection."""

import hashlib
import json

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def run() -> dict:
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    public_der = public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    fingerprint = hashlib.sha256(public_der).hexdigest()
    pss = padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    )
    message = b"This is to demonstrate the RSA-PSS signing and verification process for my Information Security Lab 4."
    signature = private_key.sign(message, pss, hashes.SHA256())
    public_key.verify(signature, message, pss, hashes.SHA256())

    changed_message_rejected = False
    try:
        public_key.verify(signature, message + b" (changed)", pss, hashes.SHA256())
    except InvalidSignature:
        changed_message_rejected = True

    checks = {
        "valid_message_verifies": True,
        "modified_message_rejected": changed_message_rejected,
    }
    return {
        "algorithm": "RSA-2048-PSS-SHA-256",
        "public_key_fingerprint_sha256": fingerprint,
        "message": message.decode("utf-8"),
        "signature_hex": signature.hex(),
        "key_material_logged": False,
        "checks": checks,
        "passed": all(checks.values()),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
