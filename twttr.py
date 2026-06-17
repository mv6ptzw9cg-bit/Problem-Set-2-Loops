text = input("Input: ")

result = ""

for letter in text:
    if letter.lower() != "a" and letter.lower() != "e" and letter.lower() != "i" and letter.lower() != "o" and letter.lower() != "u":
        result = result + letter

print("Output:", result)
