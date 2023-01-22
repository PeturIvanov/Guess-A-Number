import random

number = int(input())
computer_number = random.randint(0, 101)

while True:

    if number == computer_number:
        print("correct!")
        break
    elif number > computer_number:
        print("lower")

    elif number < computer_number:
        print("higher")

    number = int(input())


