# Transposition Cipher Encryption and Decryption

def encrypt(message, key):
    cipher = ""

    for col in range(key):
        pointer = col

        while pointer < len(message):
            cipher += message[pointer]
            pointer += key

    return cipher


def decrypt(cipher, key):
    num_cols = -(-len(cipher) // key)   # Ceiling division
    num_rows = key
    num_shaded_boxes = (num_cols * num_rows) - len(cipher)

    plaintext = [""] * num_cols

    col = 0
    row = 0

    for symbol in cipher:
        plaintext[col] += symbol
        col += 1

        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
            col = 0
            row += 1

    return "".join(plaintext)


# Main Program
message = input("Enter message: ")
key = int(input("Enter key: "))

encrypted = encrypt(message, key)
print("Encrypted Message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted Message:", decrypted)