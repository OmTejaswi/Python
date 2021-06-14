def emojies(msg):
    words = msg.split(" ")

    emoji = {
        ":)": "😄",
        ":(": "😞"
    }

    output = ""

    for word in words:
        output += emoji.get(word,word) + " "
    return output

message = input("> ")
print(emojies(message))
# print(output)