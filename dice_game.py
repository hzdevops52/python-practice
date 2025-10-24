import random

while True:
    print(f'number is : {random.randint(1,6)}')
    user_input = input('do you want to continue y/n : ')
    if user_input == 'n':
        break