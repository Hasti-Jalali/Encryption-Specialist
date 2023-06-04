# AES-CTR File Encryption and Decryption

## Description:
This project focuses on implementing AES-CTR file encryption and decryption using Python. It utilizes libraries such as `binascii`, `pbkdf2`, `os`, `pyaes`, and `secrets` to encrypt files containing student ID numbers and securely decrypt them based on user commands.

## Features:
- Encryption of files using the AES algorithm in CTR mode.
- Decryption of encrypted files with the correct key and initial vector.
- Integration of salt for key security and strength.
- Handling user commands for encryption and decryption operations.
- Generation of initial vectors using the `secrets` library.
- Key length enhancement using the `pbkdf2` library.
- Hexadecimal representation of the encryption key using the `binascii` library.
