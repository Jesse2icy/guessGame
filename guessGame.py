# Guess game 4
from random import randint
import random
import sys
import pyodbc
from collections import defaultdict

user = {'Firstname':'', 'Lastname':'', 'Score':0.0, 'pin':''}

def DBConnnection():
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-21CY202;'
                      'Database=GuessGameDB;'
                      'Trusted_Connection=yes;')


    cursor = conn.cursor()

    return cursor


def introduction():
    print('Welcome To Guess Game. ')
    login = input('Do you have a pin: ')
    while login != 'Yes' and login != 'No':
        print('Enter Yes or No once again:')
        login = input()
    

    if login == 'Yes':
        get_pin()

    elif login == 'No':
        setuserinfo()
        


def get_pin():
    pin = input('Enter your 4 digit pin: ')

    if len(pin) != 4:
        pin= input('Use 4 digits: ')
 
    else:
        return pin


    
    

def getuserinfo():
    return user

def setuserinfo():
    user_entered_pin = get_pin()
    execute = DBConnnection()
    execute.execute('SELECT * FROM UserTable')
    
    user_info = defaultdict(list)


    ## Store user information for each pin code in a list
    for row in execute:   
        user_info[row[2]].append(row[0])
        user_info[row[2]].append(row[1])
        user_info[row[2]].append(row[3])
    
    if user_entered_pin in user_info.keys():  
        for keys, values in user_info.items():
            user['Firstname'] = user_info[user_entered_pin][0]
            user['Lastname'] = user_info[user_entered_pin][1]
            user['Score'] = user_info[user_entered_pin][2]
    
    else:
        new_user()
    



def new_user():
    print('Welcome New User. Enter a new pin: ')
    user_entered_pin = get_pin()
    

    FirstName = input('Enter FirstName: ')
    LastName = input('Enter LastName: ')
    execute = DBConnnection()

    try:
       
        execute.execute('Insert into UserTable (FirstName, LastName, Pin) VALUES (?, ?, ?)', FirstName, LastName, user_entered_pin)
        execute.commit()

      
    except Exception as error:
      print(error)
    
    setuserinfo()
    




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
        difficulty_range = 40

    return (chances, difficulty_range)


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
        print('chance, '+ str(_))
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
        

    print('You lose, the number I was guessing is '+ str(val)) 





def nextround(): # starts a new round
    print('Do you want to give it another try')
    another_Round= input()
    #another_Round = ['Yes', 'No']
    while another_Round != 'Yes' and another_Round != 'No':
        print('Enter Yes or No once again:')
        another_Round = input()
    

    if another_Round == 'Yes':
        print('Here we go ', user['Firstname'])
        maingame()
        nextround()
    elif another_Round == 'No':
        print('Later Loser! ',  user['Firstname'])
        sys.exit()


#def login():
 #   maingame()





def playgame():
    
    introduction()
    #setuserinfo()
    maingame()
    nextround()

playgame()



    







    









