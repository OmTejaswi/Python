phone = input("Phone: ")

word = {
    "1": "One",
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'nine'
}

result = ''

for char in phone:
    result += word.get(char,"") + " "

print(result + "!")