import random
import secrets
import string

_ALPHABET: str = string.ascii_letters + string.digits
_ALPHABET_BYTES: bytes = _ALPHABET.encode("ascii")
_ALPHABET_LEN: int = len(_ALPHABET)


def generate_random_string(length: int = 16) -> str:
    result = bytearray(length)
    for i in range(length):
        result[i] = _ALPHABET_BYTES[random.getrandbits(6) % _ALPHABET_LEN]
    return result.decode("ascii")


def generate_secure_random_string(length: int = 16) -> str:
    result = bytearray(length)
    for i in range(length):
        result[i] = _ALPHABET_BYTES[secrets.randbelow(_ALPHABET_LEN)]
    return result.decode("ascii")
