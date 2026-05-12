# Requires: pip install pycryptodome
 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# 16-byte secret key
key = b'abcdefghijklmnop'

# Create AES cipher object
cipher = AES.new(key, AES.MODE_ECB)

# Message to encrypt
message = input("Enter message: ")

# Encrypt
encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))

# Convert encrypted data to readable format
encrypted_text = base64.b64encode(encrypted).decode()

print("Encrypted Text:", encrypted_text)

# Decrypt
decrypt_cipher = AES.new(key, AES.MODE_ECB)

decrypted = unpad(
    decrypt_cipher.decrypt(base64.b64decode(encrypted_text)),
    AES.block_size
)

print("Decrypted Text:", decrypted.decode())