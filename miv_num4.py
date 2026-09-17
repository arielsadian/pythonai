from operator import truediv

words = []
while True:
    text = input("Enter string:")
    if text == "quit":
        break
    words.append(text)
found = False
for word in words:
    if word[::-1]in words:
        found = True
        break
if found:
    print("reversed match found")
else:
    print("no reversed match found")