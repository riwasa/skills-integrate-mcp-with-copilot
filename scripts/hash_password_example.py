"""Small helper demonstrating hashing and verifying passwords with passlib.
Run: python scripts/hash_password_example.py
"""
from passlib.context import CryptContext

# Use pbkdf2_sha256 here to avoid platform-specific bcrypt C dependency issues
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


if __name__ == "__main__":
    sample = "MyS3cretPassw0rd"
    print("Sample password:", sample)
    h = hash_password(sample)
    print("Hashed:", h)
    ok = verify_password(sample, h)
    print("Verify result:", ok)
