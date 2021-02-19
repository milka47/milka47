import random

guessesTaken = 0

print("Hey there, you're pretty... What's your name?")
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I wnat to take you out on a date, but first, I want you to guess a number between 1 and 20.')

while guessesTaken < 6:
    print('Come on baby, take a guess...') 
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('no no no. WAAYYYYY TOO low.') 

    if guess > number:
        print('Oh damn, thats soooo high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Dam! Yess!!! ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print("You lost bitch. The number I was thinking of was " + number+" No date for you")
