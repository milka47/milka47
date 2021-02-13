

import random

lives = 5

words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']

secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1 
        
while lives > 0:
    print(clue)
    print('Lives left: ' + heart_symbol * lives)
    guess = input('Guess a letter or the whole word:')
    
    if guess == secret_word:
        guessed_word_correctly = True
        print('*******You WON!!!********')
        print('\N{winking face}') 
        break
        
        
    if guess in secret_word:
        print('Good One! Guess another letter\n\n')
        update_clue(guess, secret_word, clue)


    else:
        print('🙀SORRY ouy lose a life\n\n')
        lives = lives - 1

while lives == 0:
    print ("Game Over!!!")
    break
    
