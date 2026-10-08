import random
number=random.randint(1,100)
print("guess the number")
print("i choose a number")

while True:
    guess=int(input("guess a number: "))
    if guess>number:
        print("guess is too high")

    elif guess<number:
        print("guess is too low")

    else:
        print("your guess is correct , congratulations")
        break