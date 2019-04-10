#generate random number rn1
#ask for the input from the user
#store the guess in an array
#if input == rn1 end game display guesses
#else if the guesses > 7 or guess is incorrect try again

import random
rn1 = random.randint(1,25)
guesses=0
correct_guess = False

user_guesses=[]
print(rn1)
while(correct_guess == False and guesses < 7):
    guess = int(input("Guess the number dude_x222: "))
    user_guesses.append(guess)
    if(guess==rn1):
        correct_guess = True
    else:
        print("Incorrect try again: \n")
        guesses=guesses+1
        
if(correct_guess==False):
    print("You have failed")
else:
    print("You have guessed the right number")
    for x in user_guesses:
        print(x)