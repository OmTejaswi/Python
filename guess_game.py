secret_number = 9
i = 0
while i < 3:
    guess = int(input('Guess: '))
    i += 1

    if guess == int(secret_number):
        print('You won!')
        break
    elif i == 3 and guess != int(secret_number):
        print('Sorry! you failed. Try next time')

# rather then doint elif i == 3 and guess != int(secret_number) we can use else condition of while loop to doing this.
# else:
#     print('Sorry! you failed. Try next time')