# DES Algorithm Implementation in Python
# Requires: pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

# DES key must be exactly 8 bytes
key = b"12345678"

# Create DES cipher object
cipher = DES.new(key, DES.MODE_ECB)

# Plaintext
plaintext = input("Enter plaintext: ")

# Encrypt
padded_text = pad(plaintext.encode(), DES.block_size)
encrypted_text = cipher.encrypt(padded_text)

# Convert encrypted data to Base64 for display
encrypted_base64 = base64.b64encode(encrypted_text).decode()

print("\nEncrypted Text:", encrypted_base64)

# Decrypt
decrypted_padded = cipher.decrypt(base64.b64decode(encrypted_base64))
decrypted_text = unpad(decrypted_padded, DES.block_size).decode()

print("Decrypted Text:", decrypted_text)