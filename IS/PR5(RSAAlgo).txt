# RSA Algorithm Implementation in Python

# Function to find gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

# Step 1: Choose two prime numbers
p = 17
q = 11

# Step 2: Compute n
n = p * q

# Step 3: Compute Euler Totient Function
phi = (p - 1) * (q - 1)

# Step 4: Choose e such that gcd(e, phi) = 1
e = 7

# Step 5: Compute d
d = mod_inverse(e, phi)

print("Public Key (e, n) =", (e, n))
print("Private Key (d, n) =", (d, n))

# Message to encrypt
msg = int(input("Enter message (number): "))

# Encryption
cipher = (msg ** e) % n
print("Encrypted Message =", cipher)

# Decryption
plain = (cipher ** d) % n
print("Decrypted Message =", plain)


