#This version has been written from scratch, by memory.

# import random number. Not for now

print "Guesser game by Mylo"

def main(): #defines and runs the main set of functions below

    print "Guess a number between 1 and 100."
    setNumber = 50 #set as 50 for now, can be random.randint(1,100) once random module is imported https://docs.python.org/2/library/random.html
    found = False
    while not found:
        userGuess = input ("Your guess: ")
        if userGuess == setNumber: #As I rewrote this I forgot about the colon on the end. Needs to be remembered
            print "Thats correct!"
            found = True #Can't be forgotten also
        elif userGuess < setNumber: #elif can't be printed with a colon because there's already 1 in the statement
            print "Incorrect! Try again."
        else:
            print "Guess higher."

if __name__ == "__main__":
    main()
