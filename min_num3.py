def camel_to_hyphen(text):
    result = ""
    for char in text:
        if char.isupper():
            result += "-" + char.lower()
        else:
            result += char
    return result
print(camel_to_hyphen("helloPython"))