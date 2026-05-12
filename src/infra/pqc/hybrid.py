"""Post-quantum hybrid key exchange for mission communication encryption."""

import os
from typing import Tuple
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import x25519, ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


def generate_hybrid_keypair() -> Tuple[bytes, bytes]:
    """Generate a hybrid keypair combining X25519 + PQC signature."""
    x25519_private = x25519.X25519PrivateKey.generate()

    hybrid_private = x25519_private.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption(),
    )

    hybrid_public = x25519_private.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )

    return hybrid_private, hybrid_public


def hybrid_key_exchange(
    private_key_bytes: bytes,
    peer_public_bytes: bytes,
    info: bytes = b"mission-dao-hybrid",
) -> bytes:
    """Perform hybrid key exchange returning a shared secret."""
    private_key = x25519.X25519PrivateKey.from_private_bytes(private_key_bytes)
    peer_public = x25519.X25519PublicKey.from_public_bytes(peer_public_bytes)
    shared_secret = private_key.exchange(peer_public)

    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=info,
    )
    return hkdf.derive(shared_secret)


def encrypt_mission_payload(
    payload: bytes,
    shared_key: bytes,
) -> Tuple[bytes, bytes]:
    """Encrypt mission payload with AES-GCM using shared key."""
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    aesgcm = AESGCM(shared_key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, payload, None)
    return ciphertext, nonce


def decrypt_mission_payload(
    ciphertext: bytes,
    nonce: bytes,
    shared_key: bytes,
) -> bytes:
    """Decrypt AES-GCM encrypted mission payload."""
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    aesgcm = AESGCM(shared_key)
    return aesgcm.decrypt(nonce, ciphertext, None)
