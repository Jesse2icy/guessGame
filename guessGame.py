# Guess game 4
# Implement a Hard Mode

from random import randint
import random

def introduction():
    print('Welcome to GuessGame. Ready for the challenge. Enter name:')
    username = input('')
    print('Welcome ', username)

def maingame():
    chance , diff_range = difficulty()

    val = random.randint (0,diff_range)

    print('Enter a prediction between 0 and '+ str(diff_range)) 
    user_guess = int(input())

    for _ in range(chance):
        if val == user_guess:
            print('You win')
    
            return
        elif user_guess < val:
            print ('go higher')
        else:
            print ('go lower')
        
        user_guess = int(input())
    print('you lose!!')


def difficulty():
    print('Choose Your difficult. 1 for easy. 2 for medium.  3 for hard :')
    game_difficulty = int(input())

    while game_difficulty != 1 and game_difficulty != 2 and game_difficulty != 3:
        print('Hey idiot, use only 1 , 2 or 3! Enter once again:') ## This tells the user to input the right number.
        game_difficulty = int(input())

    chances = 0
    difficulty_range = 0

    if game_difficulty == 1:
        chances = 5
        difficulty_range = 10
    elif game_difficulty == 2:
        chances = 5
        difficulty_range = 20
    else:
        chances = 10
        difficulty_range = 80

    return (chances, difficulty_range)

def playgame():
    introduction()
    maingame()
    
### Game Starts Here
playgame()


