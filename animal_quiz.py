def check_guess(guess, answer):
    global score
    global guess1
    global guess2

    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Hell Yeah!!! OMG, Your are Correct answer. \nNext Question: \n \n')
            score = score + 1
            still_guessing = False 
        
        else:
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again: ') 
            attempt = attempt + 1 

    if attempt == 3:
        print('You tried ALL 3 attemps, the correct answer is ' + answer +'\n \n') 

        
score = 0 
print('Guess the Animal!')
guess1 = input('#1. Which bear lives at the North Pole? ')
check_guess(guess1, 'polar bear') 
guess2 = input('#2. Which is the fastest land animal? ') 
check_guess(guess2, 'cheetah')
guess3 = input('#3. Which is the largest animal? ')
check_guess(guess3, 'blue whale') 


print('Your score is ' + str(int((score/3)*100)) +'%') 


