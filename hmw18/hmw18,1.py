def toggle_text(text: str) -> str:
    result = ""
    for ch in text:
        code = ord(ch)
        if 65 <= code <= 90:
            result += chr(code + 32)
        elif 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += ch
    return result

# Test
print(toggle_text("Hello World!"))   # hELLO wORLD!
print(toggle_text("Python3.11"))     # pYTHON3.11