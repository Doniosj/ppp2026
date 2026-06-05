def caesar_encode(text: str, shift: int = 3) -> str:
    result = ""
    for ch in text:
        code = ord(ch)
        if 65 <= code <= 90:
            result += chr((code - 65 + shift) % 26 + 65)
        elif 97 <= code <= 122:
            result += chr((code - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result


def caesar_decode(text: str, shift: int = 3) -> str:
    return caesar_encode(text, -shift)


# Test
print(caesar_encode("ABC"))         # DEF
print(caesar_encode("ABC", 3))      # DEF
print(caesar_decode("Def"))         # Abc
print(caesar_decode("Def", 3))      # Abc
print(caesar_encode("XYZ"))         # ABC
print(caesar_encode("Hello!"))      # Khoor!
print(caesar_decode("Khoor!"))      # Hello!