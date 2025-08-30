# Simple Password Manager (Python)

A lightweight password manager built with **Python** and **cryptography.fernet**.  
It lets you securely store and view your passwords using a master password.

---

## Features
- Encrypts and decrypts passwords with a master password.
- Uses `PBKDF2HMAC` for secure key derivation.
- Simple CLI for adding and viewing saved accounts.
- Stores data in a local text file (`passwords.txt`).

---

## Requirements
- Python 3.8+
- [cryptography](https://pypi.org/project/cryptography/)

Install dependencies:
```bash
pip install cryptography
