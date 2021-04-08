# Guess game 4
from random import randint
import random

# Introduce the user
def introduction():
    print('Welcome to GuessGame. Ready for the challenge. Enter name:')
    username = str(input())   # the next change will be username must contain certain characters
    print('Welcome ', username)

# This is the main logic of the game 
def maingame():
    chance , diff_range = difficulty()
    val = random.randint (0,diff_range)

    print('Enter a prediction between 0 and '+ str(diff_range)) 

    ## Putting a string here breaks the game. Could you come up with a fix? --> I think I fixed it.
    try:
        user_guess = int(input())
    except ValueError:
        print('Error use integers only. Try Again!')
        user_guess = int(input())
    

    for _ in range(chance):
        if val == user_guess:
            print('You win, I was guessing '+ str(val))
    
            return
        elif user_guess < val:
            print ('go higher')
        else:
            print ('go lower')
        try:
            user_guess = int(input())
        except ValueError:
            print('Error use integers only. Try Again')
            user_guess = int(input())
        

    print('You lose, the number I was guessing is '+ str(val)) # the change you asked for.


def difficulty():
    try:                                    # I used a try statement so my program doesn't crash when user types two instead of 2
                                            # I was still able to crash your program typing two --> fixed
        print('Choose Your difficult. 1 for easy. 2 for medium.  3 for hard :')
        global game_difficulty               # i made this global variable because I also used it in the loop.  -->   What loop ? --> the while loop in the difficulty function.
        game_difficulty = int(input())
    except ValueError:
        print('Error: Use Integers Only')
        game_difficulty = int(input())

    while game_difficulty != 1 and game_difficulty != 2 and game_difficulty != 3:
        print('Hey idiot, use only 1 , 2 or 3! Enter once again:') ## This tells the user to input the right number.
        game_difficulty = int(input())

    chances = 0
    difficulty_range = 0

    if game_difficulty == 1:
        chances = 4                # the user was getting 6 tries since the initial input was not part of the chances.To solve that I decrease the chances by 1.
        difficulty_range = 10
    elif game_difficulty == 2:
        chances = 4
        difficulty_range = 20
    else:
        chances = 9
        difficulty_range = 80

    return (chances, difficulty_range)

def playgame():
    introduction()
    maingame()
    
### Game Starts Here
playgame()


