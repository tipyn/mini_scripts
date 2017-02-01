import random

guessesTaken = 0
print('Hello! What is your name?')
myName = raw_input()
number = random.randint(1, 20)
print('Hey ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Guess which one')
    guess = raw_input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Nope, too low')
    if guess > number:
        print('Nope, too high')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Yay ' + myName + '! You guessed it in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
