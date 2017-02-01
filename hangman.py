import time

name = raw_input("Hi! What's your name? ")

# I don't know how to add a comma after name??
print "Hey, " + name,"wanna play hangman with me?"

print ""

# wait for 1 second
time.sleep(1)

print "Guess some letters..."
time.sleep(0.5)

# secret word
word = "chicken"

#creates an variable with an empty value
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

    # set the players guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:

     # turns counter decreases with 1 (now 9)
        turns -= 1

        print "nope"

    # how many turns are left
        print "You have", + turns, 'more guesses'

    # if the turns are equal to zero
        if turns == 0:

        # print "You Loose"
            print "You Loose"
