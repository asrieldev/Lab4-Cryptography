"""Exercise 1: compare AES-GCM and AES-CBC encryption modes."""

import json
import os

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import padding as symmetric_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def run() -> dict:
    plaintext = b"Lab 4: protect this confidential message."
    associated_data = b"course=information-security;exercise=AES-GCM"

    key = AESGCM.generate_key(bit_length=256)
    nonce = os.urandom(12)
    cipher = AESGCM(key)
    ciphertext = cipher.encrypt(nonce, plaintext, associated_data)
    recovered = cipher.decrypt(nonce, ciphertext, associated_data)

    changed = bytearray(ciphertext)
    changed[0] ^= 1
    tampering_rejected = False
    try:
        cipher.decrypt(nonce, bytes(changed), associated_data)
    except InvalidTag:
        tampering_rejected = True

    key_size_comparison = []
    for bits in (128, 256):
        comparison_key = AESGCM.generate_key(bit_length=bits)
        comparison_nonce = os.urandom(12)
        comparison_cipher = AESGCM(comparison_key)
        comparison_ct = comparison_cipher.encrypt(comparison_nonce, plaintext, associated_data)
        comparison_pt = comparison_cipher.decrypt(comparison_nonce, comparison_ct, associated_data)
        key_size_comparison.append({
            "key_bits": bits,
            "round_trip_matches": comparison_pt == plaintext,
            "ciphertext_and_tag_bytes": len(comparison_ct),
        })

    # Educational mode comparison only: bare CBC does not authenticate data.
    cbc_key = os.urandom(32)
    iv = os.urandom(16)
    padder = symmetric_padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    encryptor = Cipher(algorithms.AES(cbc_key), modes.CBC(iv)).encryptor()
    cbc_ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    decryptor = Cipher(algorithms.AES(cbc_key), modes.CBC(iv)).decryptor()
    padded_recovered = decryptor.update(cbc_ciphertext) + decryptor.finalize()
    unpadder = symmetric_padding.PKCS7(algorithms.AES.block_size).unpadder()
    cbc_recovered = unpadder.update(padded_recovered) + unpadder.finalize()

    checks = {
        "gcm_decryption_matches": recovered == plaintext,
        "gcm_tampering_rejected": tampering_rejected,
        "aes_128_and_256_gcm_round_trip": all(x["round_trip_matches"] for x in key_size_comparison),
        "aes_256_cbc_round_trip": cbc_recovered == plaintext,
    }
    return {
        "algorithm": "AES-256-GCM",
        "key_bits": len(key) * 8,
        "nonce_hex": nonce.hex(),
        "associated_data": associated_data.decode("ascii"),
        "plaintext": plaintext.decode("utf-8"),
        "recovered_plaintext": recovered.decode("utf-8"),
        "ciphertext_and_tag_hex": ciphertext.hex(),
        "key_material_logged": False,
        "key_size_comparison": key_size_comparison,
        "cbc_mode_comparison": {
            "algorithm": "AES-256-CBC with PKCS7 padding",
            "iv_hex": iv.hex(),
            "ciphertext_bytes": len(cbc_ciphertext),
            "round_trip_matches": cbc_recovered == plaintext,
            "authenticated": False,
            "warning": "Bare CBC provides no integrity; prefer an authenticated mode such as GCM.",
        },
        "checks": checks,
        "passed": all(checks.values()),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))

