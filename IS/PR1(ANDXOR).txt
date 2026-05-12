# String value
text = "Hello World9"

print("AND with 127:")
for ch in text:
    result = ord(ch) & 127
    print(chr(result), end="")

print("\n")

print("Character  XOR with 127")
for ch in text:
    xor_value = ord(ch) ^ 127
    print(ch, " --> ", xor_value)