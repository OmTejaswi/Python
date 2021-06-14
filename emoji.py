messgae = input("> ")
words = messgae.split(" ")

emoji = {
    ":)": "😄",
    ":(": "😞"
}

output = ""

for word in words:
    output += emoji.get(word,word) + " "

print(output)