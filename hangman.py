import time

name = raw_input("Hi! What's your name? ")

# I don't know how to add a comma after name??
print "Hey " + name,"wanna play hangman with me?"
print ""
time.sleep(1)
print "Guess some letters..."
time.sleep(0.5)

# secret word
word = "chicken"

guesses = ''
turns = 10

# Create a while loop
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print char,
        else:
            print "_",
            failed += 1
    if failed == 0:
        print "You won"
        break
    print

    # ask the player to guess a character
    guess = raw_input("guess a character:")

    # add the players guess to guesses
    guesses += guess

    if guess not in word:
        turns -= 1
        print "nope"
        print "You have", + turns, 'more guesses'
        if turns == 0:
            print "Gosh darn it."
