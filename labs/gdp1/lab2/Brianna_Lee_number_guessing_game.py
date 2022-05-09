import random

secret_number = random.randrange(1,129)
# for debugging
print(secret_number)

guesses = []
maxTries = 7
guess = "0"
stop = False

while guess != secret_number:
    guess = input("Guess a number 1 to 128: ")
    guesses.append(guess)
    if guess == "Q":
        stop = True
        print("Thanks for playing!")
        break
    guess = int(guess)
    if len(guesses) > maxTries:
        print("Exceeded the number of tries.")
        break
    elif int(guess) < secret_number:
        print("Too low.")
    elif int(guess) > secret_number:
        print("Too high.")
    else:
        print("Correct!")
        print("Your guesses: ")
        for i in guesses:
            print(i, end= " ")

