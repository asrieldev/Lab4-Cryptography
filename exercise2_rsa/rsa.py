"""Exercise 2: RSA-OAEP encryption and key-size comparison."""

import hashlib
import json

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
    oaep = padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )
    plaintext = b"RSA-OAEP protects a short session secret."
    ciphertext = public_key.encrypt(plaintext, oaep)
    recovered = private_key.decrypt(ciphertext, oaep)

    changed = bytearray(ciphertext)
    changed[-1] ^= 1
    tampering_rejected = False
    try:
        private_key.decrypt(bytes(changed), oaep)
    except ValueError:
        tampering_rejected = True

    size_comparison = []
    for bits in (2048, 3072):
        comparison_private = rsa.generate_private_key(public_exponent=65537, key_size=bits)
        comparison_public = comparison_private.public_key()
        comparison_ciphertext = comparison_public.encrypt(plaintext, oaep)
        comparison_plaintext = comparison_private.decrypt(comparison_ciphertext, oaep)
        size_comparison.append({
            "key_bits": bits,
            "ciphertext_bytes": len(comparison_ciphertext),
            "round_trip_matches": comparison_plaintext == plaintext,
        })

    checks = {
        "decryption_matches": recovered == plaintext,
        "modified_ciphertext_rejected": tampering_rejected,
        "rsa_2048_and_3072_round_trip": all(x["round_trip_matches"] for x in size_comparison),
    }
    return {
        "algorithm": "RSA-2048-OAEP-SHA-256",
        "public_key_fingerprint_sha256": fingerprint,
        "plaintext": plaintext.decode("utf-8"),
        "ciphertext_hex": ciphertext.hex(),
        "key_material_logged": False,
        "key_size_comparison": size_comparison,
        "checks": checks,
        "passed": all(checks.values()),
        "note": "RSA-OAEP is for short inputs; use hybrid encryption for bulk data.",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
