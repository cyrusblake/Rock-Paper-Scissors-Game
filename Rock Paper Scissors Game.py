#Rock Paper Scissors game

"""
from tkinter import *

window = Tk()
window.title("Letters into binary code")
window.configure(background="blue")

window.mainloop()
"""

import random

modes = ['1', '2']

r = 'Rock' 
p = 'Paper' 
s = 'Scissors'

pos1 = ['rock', 'paper', 'scissors']

tie = ['rock Vs Rock', 'paper Vs Paper', 'scissors Vs Scissors']
win = ['rock Vs Scissors', 'paper Vs Rock', 'scissors Vs Paper']
lost = ['rock Vs Paper', 'paper Vs Scissors', 'scissors Vs Rock']


mode = input('Pick a mode to play. Mode 1 or Mode 2?: ')

while mode not in modes:
    print('\nPlease pick a mode ')
    mode = input('Pick a mode to play. Mode 1 or Mode 2?: ')


if mode == modes[0]:
    user = input('\nRock paper scissors says shoot! ')
    while user not in pos1:
        print('Please type a proper answer and please use lower case letters.\n')
        user = input('\nRock paper scissors says shoot! ')

    game = (user + ' Vs ' + random.choice([r,p,s]))
    print('\n' + game)

    if game in win:
        print('You Win')
    elif game in lost:
        print('You Lost')

    
    while game not in win and game not in lost:
        print('Its a tie go again')

        user = input('\nRock paper scissors says shoot! ')
        while user not in pos1:
             print('Please type a proper answer and please use lower case letters.\n')
             user = input('\nRock paper scissors says shoot! ')

        game = (user + ' Vs ' + random.choice([r,p,s]))
        print('\n' + game)

        if game in win:
            print('You Win')
        elif game in lost:
            print('You Lost')


#next mode..........................................................................................


if mode == modes[1]:
    user1 = input('\nRock paper scissors says shoot! ')
    user2 = input('\nRock paper scissors says shoot! ')
    user3 = input('\nRock paper scissors says shoot! ')


    while user1 not in pos1:
        print('Please type a proper answer and please use lower case letters.\n')
        user1 = input('\nRock paper scissors says shoot! ')

    while user2 not in pos1:
        print('Please type a proper answer and please use lower case letters.\n')
        user2 = input('\nRock paper scissors says shoot! ')

    while user3 not in pos1:
        print('Please type a proper answer and please use lower case letters.\n')
        user3 = input('\nRock paper scissors says shoot! ')

    game1 = (user1 + ' Vs ' + random.choice([r,p,s])) 
    game2 = (user2 + ' Vs ' + random.choice([r,p,s]))
    game3 = (user3 + ' Vs ' + random.choice([r,p,s]))

    print('\n\n' + game1 + '               ' + game2 + '               ' + game3)
  
#DOUBLE WINS

    if game1 in lost and game2 in win and game3 in win: #lost win win
        print('You Win')
    elif game1 in win and game2 in lost and game3 in win: #win lost win
        print('You Win')
    elif game1 in win and game2 in win and game3 in lost: #win win lost
        print('You Win')

                                                       
    if game1 in tie and game2 in win and game3 in win:  #tie win win
        print('You Win')
    elif game1 in win and game2 in tie and game3 in win: #win tie win
        print('You Win')
    elif game1 in win and game2 in win and game3 in tie: #win win tie 
        print('You Win')

    if game1 in win and game2 in win and game3 in win:
        print('You Win')

#DOUBLE LOST

                                                      
    if game1 in win and game2 in lost and game3 in lost: #win lost lost  
        print('You Lost')
    elif game1 in lost and game2 in win and game3 in lost: #lost win lost 
        print('You Lost')
    elif game1 in lost and game2 in lost and game3 in win: #lost lost win  
        print('You Lost')

                                                  
    if game1 in tie and game2 in lost and game3 in lost: #tie lost lost  
        print('You Lost')
    elif game1 in lost and game2 in tie and game3 in lost: #lost tie lost
        print('You Lost')
    elif game1 in lost and game2 in lost and game3 in tie:  #lost lost tie
        print('You Lost')

    if game1 in lost and game2 in lost and game3 in lost: #lost lost lost
        print('You Lost')

#DOUBLE TIE

    if game1 in tie and game2 in tie and game3 in win: #tie tie win 
        print('You Win')
    elif game1 in tie and game2 in tie and game3 in lost: #tie tie lost
        print('You Lost')







    #win tie tie   

    while game1 in win and game2 in tie and game3 in tie:
        print('\nIts a tie')
        print('Go again')

        user1 = input('\nRock paper scissors says shoot! ')
        user2 = input('\nRock paper scissors says shoot! ')
        user3 = input('\nRock paper scissors says shoot! ')

        while user1 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user1 = input('\nRock paper scissors says shoot! ')

        while user2 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user2 = input('\nRock paper scissors says shoot! ')

        while user3 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user3 = input('\nRock paper scissors says shoot! ')

        game1 = (user1 + ' Vs ' + random.choice([r,p,s])) 
        game2 = (user2 + ' Vs ' + random.choice([r,p,s]))
        game3 = (user3 + ' Vs ' + random.choice([r,p,s]))

        print('\n' + game1 + '               ' + game2 + '               ' + game3)

        #DOUBLE WINS

        if game1 in lost and game2 in win and game3 in win: #lost win win
             print('You Win')
        elif game1 in win and game2 in lost and game3 in win: #win lost win
            print('You Win')
        elif game1 in win and game2 in win and game3 in lost: #win win lost
            print('You Win')

                                                       
        if game1 in tie and game2 in win and game3 in win:  #tie win win
            print('You Win')
        elif game1 in win and game2 in tie and game3 in win: #win tie win
            print('You Win')
        elif game1 in win and game2 in win and game3 in tie:#win win tie 
            print('You Win')

        if game1 in win and game2 in win and game3 in win: #win win win
            print('You Win')

#DOUBLE LOST

                                                      
        if game1 in win and game2 in lost and game3 in lost: #win lost lost  
            print('You Lost')
        elif game1 in lost and game2 in win and game3 in lost: #lost win lost 
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in win: #lost lost win  
            print('You Lost')

                                                  
        if game1 in tie and game2 in lost and game3 in lost: #tie lost lost  
            print('You Lost')
        elif game1 in lost and game2 in tie and game3 in lost: #lost tie lost
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in tie:  #lost lost tie
            print('You Lost')

        if game1 in lost and game2 in lost and game3 in lost: #lost lost lost
            print('You Lost')

#DOUBLE TIE


        if game1 in tie and game2 in tie and game3 in win: #tie tie win 
            print('You Win')
        elif game1 in tie and game2 in tie and game3 in lost: #tie tie lost
            print('You Lost')








    #lost tie tie 

    while game1 in lost and game2 in tie and game3 in tie:
        print('\nIts a tie')
        print('Go again')

        user1 = input('\nRock paper scissors says shoot! ')
        user2 = input('\nRock paper scissors says shoot! ')
        user3 = input('\nRock paper scissors says shoot! ')

        while user1 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user1 = input('\nRock paper scissors says shoot! ')

        while user2 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user2 = input('\nRock paper scissors says shoot! ')

        while user3 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user3 = input('\nRock paper scissors says shoot! ')

        game1 = (user1 + ' Vs ' + random.choice([r,p,s])) 
        game2 = (user2 + ' Vs ' + random.choice([r,p,s]))
        game3 = (user3 + ' Vs ' + random.choice([r,p,s]))

        print('\n' + game1 + '               ' + game2 + '               ' + game3)


        #DOUBLE WINS

        if game1 in lost and game2 in win and game3 in win: #lost win win
             print('You Win')
        elif game1 in win and game2 in lost and game3 in win: #win lost win
            print('You Win')
        elif game1 in win and game2 in win and game3 in lost: #win win lost
            print('You Win')

                                                       
        if game1 in tie and game2 in win and game3 in win:  #tie win win
            print('You Win')
        elif game1 in win and game2 in tie and game3 in win: #win tie win
            print('You Win')
        elif game1 in win and game2 in win and game3 in tie:#win win tie 
            print('You Win')

        if game1 in win and game2 in win and game3 in win: #win win win
            print('You Win')

#DOUBLE LOST

                                                      
        if game1 in win and game2 in lost and game3 in lost: #win lost lost  
            print('You Lost')
        elif game1 in lost and game2 in win and game3 in lost: #lost win lost 
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in win: #lost lost win  
            print('You Lost')

                                                  
        if game1 in tie and game2 in lost and game3 in lost: #tie lost lost  
            print('You Lost')
        elif game1 in lost and game2 in tie and game3 in lost: #lost tie lost
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in tie:  #lost lost tie
            print('You Lost')

        if game1 in lost and game2 in lost and game3 in lost: #lost lost lost
            print('You Lost')

#DOUBLE TIE


        if game1 in tie and game2 in tie and game3 in win: #tie tie win 
            print('You Win')
        elif game1 in tie and game2 in tie and game3 in lost: #tie tie lost
            print('You Lost')








    #win lost tie

    while game1 in win and game2 in lost and game3 in tie:
        print('\nIts a tie')
        print('Go again')

        user1 = input('\nRock paper scissors says shoot! ')
        user2 = input('\nRock paper scissors says shoot! ')
        user3 = input('\nRock paper scissors says shoot! ')

        while user1 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user1 = input('\nRock paper scissors says shoot! ')

        while user2 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user2 = input('\nRock paper scissors says shoot! ')

        while user3 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user3 = input('\nRock paper scissors says shoot! ')

        game1 = (user1 + ' Vs ' + random.choice([r,p,s])) 
        game2 = (user2 + ' Vs ' + random.choice([r,p,s]))
        game3 = (user3 + ' Vs ' + random.choice([r,p,s]))

        print('\n' + game1 + '               ' + game2 + '               ' + game3)

        #DOUBLE WINS

        if game1 in lost and game2 in win and game3 in win: #lost win win
             print('You Win')
        elif game1 in win and game2 in lost and game3 in win: #win lost win
            print('You Win')
        elif game1 in win and game2 in win and game3 in lost: #win win lost
            print('You Win')

                                                       
        if game1 in tie and game2 in win and game3 in win:  #tie win win
            print('You Win')
        elif game1 in win and game2 in tie and game3 in win: #win tie win
            print('You Win')
        elif game1 in win and game2 in win and game3 in tie:#win win tie 
            print('You Win')

        if game1 in win and game2 in win and game3 in win: #win win win
            print('You Win')

#DOUBLE LOST

                                                      
        if game1 in win and game2 in lost and game3 in lost: #win lost lost  
            print('You Lost')
        elif game1 in lost and game2 in win and game3 in lost: #lost win lost 
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in win: #lost lost win  
            print('You Lost')

                                                  
        if game1 in tie and game2 in lost and game3 in lost: #tie lost lost  
            print('You Lost')
        elif game1 in lost and game2 in tie and game3 in lost: #lost tie lost
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in tie:  #lost lost tie
            print('You Lost')

        if game1 in lost and game2 in lost and game3 in lost: #lost lost lost
            print('You Lost')

#DOUBLE TIE


        if game1 in tie and game2 in tie and game3 in win: #tie tie win 
            print('You Win')
        elif game1 in tie and game2 in tie and game3 in lost: #tie tie lost
            print('You Lost')



     #win tie lost

    while game1 in win and game2 in lost and game3 in tie:
        print('\nIts a tie')
        print('Go again')

        user1 = input('\nRock paper scissors says shoot! ')
        user2 = input('\nRock paper scissors says shoot! ')
        user3 = input('\nRock paper scissors says shoot! ')

        while user1 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user1 = input('\nRock paper scissors says shoot! ')

        while user2 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user2 = input('\nRock paper scissors says shoot! ')

        while user3 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user3 = input('\nRock paper scissors says shoot! ')

        game1 = (user1 + ' Vs ' + random.choice([r,p,s])) 
        game2 = (user2 + ' Vs ' + random.choice([r,p,s]))
        game3 = (user3 + ' Vs ' + random.choice([r,p,s]))
 
        print('\n' + game1 + '               ' + game2 + '               ' + game3)

           #DOUBLE WINS

        if game1 in lost and game2 in win and game3 in win: #lost win win
            print('You Win')
        elif game1 in win and game2 in lost and game3 in win: #win lost win
            print('You Win')
        elif game1 in win and game2 in win and game3 in lost: #win win lost
            print('You Win')

                                                       
        if game1 in tie and game2 in win and game3 in win:  #tie win win
            print('You Win')
        elif game1 in win and game2 in tie and game3 in win: #win tie win
            print('You Win')
        elif game1 in win and game2 in win and game3 in tie:#win win tie 
            print('You Win')

        if game1 in win and game2 in win and game3 in win: #win win win
            print('You Win')

#DOUBLE LOST

                                                      
        if game1 in win and game2 in lost and game3 in lost: #win lost lost  
            print('You Lost')
        elif game1 in lost and game2 in win and game3 in lost: #lost win lost 
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in win: #lost lost win  
            print('You Lost')

                                                  
        if game1 in tie and game2 in lost and game3 in lost: #tie lost lost  
            print('You Lost')
        elif game1 in lost and game2 in tie and game3 in lost: #lost tie lost
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in tie:  #lost lost tie
            print('You Lost')

        if game1 in lost and game2 in lost and game3 in lost: #lost lost lost
            print('You Lost')

#DOUBLE TIE


        if game1 in tie and game2 in tie and game3 in win: #tie tie win 
            print('You Win')
        elif game1 in tie and game2 in tie and game3 in lost: #tie tie lost
            print('You Lost')

        








#lost win tie

    while game1 in lost and game2 in win and game3 in tie:
        print('\nIts a tie')
        print('Go again')

        user1 = input('\nRock paper scissors says shoot! ')
        user2 = input('\nRock paper scissors says shoot! ')
        user3 = input('\nRock paper scissors says shoot! ')

        while user1 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user1 = input('\nRock paper scissors says shoot! ')

        while user2 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user2 = input('\nRock paper scissors says shoot! ')

        while user3 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user3 = input('\nRock paper scissors says shoot! ')

        game1 = (user1 + ' Vs ' + random.choice([r,p,s])) 
        game2 = (user2 + ' Vs ' + random.choice([r,p,s]))
        game3 = (user3 + ' Vs ' + random.choice([r,p,s]))

        print('\n' + game1 + '               ' + game2 + '               ' + game3)



        #DOUBLE WINS

        if game1 in lost and game2 in win and game3 in win: #lost win win
             print('You Win')
        elif game1 in win and game2 in lost and game3 in win: #win lost win
            print('You Win')
        elif game1 in win and game2 in win and game3 in lost: #win win lost
            print('You Win')

                                                       
        if game1 in tie and game2 in win and game3 in win:  #tie win win
            print('You Win')
        elif game1 in win and game2 in tie and game3 in win: #win tie win
            print('You Win')
        elif game1 in win and game2 in win and game3 in tie:#win win tie 
            print('You Win')

        if game1 in win and game2 in win and game3 in win: #win win win
            print('You Win')

#DOUBLE LOST

                                                      
        if game1 in win and game2 in lost and game3 in lost: #win lost lost  
            print('You Lost')
        elif game1 in lost and game2 in win and game3 in lost: #lost win lost 
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in win: #lost lost win  
            print('You Lost')

                                                  
        if game1 in tie and game2 in lost and game3 in lost: #tie lost lost  
            print('You Lost')
        elif game1 in lost and game2 in tie and game3 in lost: #lost tie lost
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in tie:  #lost lost tie
            print('You Lost')

        if game1 in lost and game2 in lost and game3 in lost: #lost lost lost
            print('You Lost')

#DOUBLE TIE


        if game1 in tie and game2 in tie and game3 in win: #tie tie win 
            print('You Win')
        elif game1 in tie and game2 in tie and game3 in lost: #tie tie lost
            print('You Lost')










    #tie lost win

    while game1 in tie and game2 in lost and game3 in win:
        print('\nIts a tie')
        print('Go again')

        user1 = input('\nRock paper scissors says shoot! ')
        user2 = input('\nRock paper scissors says shoot! ')
        user3 = input('\nRock paper scissors says shoot! ')

        while user1 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user1 = input('\nRock paper scissors says shoot! ')

        while user2 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user2 = input('\nRock paper scissors says shoot! ')

        while user3 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user3 = input('\nRock paper scissors says shoot! ')

        game1 = (user1 + ' Vs ' + random.choice([r,p,s])) 
        game2 = (user2 + ' Vs ' + random.choice([r,p,s]))
        game3 = (user3 + ' Vs ' + random.choice([r,p,s]))

        print('\n' + game1 + '               ' + game2 + '               ' + game3)


       #DOUBLE WINS

        if game1 in lost and game2 in win and game3 in win: #lost win win
             print('You Win')
        elif game1 in win and game2 in lost and game3 in win: #win lost win
            print('You Win')
        elif game1 in win and game2 in win and game3 in lost: #win win lost
            print('You Win')

                                                       
        if game1 in tie and game2 in win and game3 in win:  #tie win win
            print('You Win')
        elif game1 in win and game2 in tie and game3 in win: #win tie win
            print('You Win')
        elif game1 in win and game2 in win and game3 in tie:#win win tie 
            print('You Win')

        if game1 in win and game2 in win and game3 in win: #win win win
            print('You Win')

#DOUBLE LOST

                                                      
        if game1 in win and game2 in lost and game3 in lost: #win lost lost  
            print('You Lost')
        elif game1 in lost and game2 in win and game3 in lost: #lost win lost 
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in win: #lost lost win  
            print('You Lost')

                                                  
        if game1 in tie and game2 in lost and game3 in lost: #tie lost lost  
            print('You Lost')
        elif game1 in lost and game2 in tie and game3 in lost: #lost tie lost
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in tie:  #lost lost tie
            print('You Lost')

        if game1 in lost and game2 in lost and game3 in lost: #lost lost lost
            print('You Lost')

#DOUBLE TIE


        if game1 in tie and game2 in tie and game3 in win: #tie tie win 
            print('You Win')
        elif game1 in tie and game2 in tie and game3 in lost: #tie tie lost
            print('You Lost')
 











    #tie win lost

    while game1 in tie and game2 in win and game3 in lost:
        print('\nIts a tie')
        print('Go again')

        user1 = input('\nRock paper scissors says shoot! ')
        user2 = input('\nRock paper scissors says shoot! ')
        user3 = input('\nRock paper scissors says shoot! ')

        while user1 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user1 = input('\nRock paper scissors says shoot! ')

        while user2 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user2 = input('\nRock paper scissors says shoot! ')

        while user3 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user3 = input('\nRock paper scissors says shoot! ')

        game1 = (user1 + ' Vs ' + random.choice([r,p,s])) 
        game2 = (user2 + ' Vs ' + random.choice([r,p,s]))
        game3 = (user3 + ' Vs ' + random.choice([r,p,s]))

        print('\n' + game1 + '               ' + game2 + '               ' + game3)

        #DOUBLE WINS

        if game1 in lost and game2 in win and game3 in win: #lost win win
             print('You Win')
        elif game1 in win and game2 in lost and game3 in win: #win lost win
            print('You Win')
        elif game1 in win and game2 in win and game3 in lost: #win win lost
            print('You Win')

                                                       
        if game1 in tie and game2 in win and game3 in win:  #tie win win
            print('You Win')
        elif game1 in win and game2 in tie and game3 in win: #win tie win
            print('You Win')
        elif game1 in win and game2 in win and game3 in tie:#win win tie 
            print('You Win')

        if game1 in win and game2 in win and game3 in win: #win win win
            print('You Win')

#DOUBLE LOST

                                                      
        if game1 in win and game2 in lost and game3 in lost: #win lost lost  
            print('You Lost')
        elif game1 in lost and game2 in win and game3 in lost: #lost win lost 
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in win: #lost lost win  
            print('You Lost')

                                                  
        if game1 in tie and game2 in lost and game3 in lost: #tie lost lost  
            print('You Lost')
        elif game1 in lost and game2 in tie and game3 in lost: #lost tie lost
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in tie:  #lost lost tie
            print('You Lost')

        if game1 in lost and game2 in lost and game3 in lost: #lost lost lost
            print('You Lost')

#DOUBLE TIE


        if game1 in tie and game2 in tie and game3 in win: #tie tie win 
            print('You Win')
        elif game1 in tie and game2 in tie and game3 in lost: #tie tie lost
            print('You Lost')








     #tie tie tie

    while game1 in tie and game2 in tie and game3 in tie:
        print('\nIts a tie')
        print('Go again')

        user1 = input('\nRock paper scissors says shoot! ')
        user2 = input('\nRock paper scissors says shoot! ')
        user3 = input('\nRock paper scissors says shoot! ')  
  
     
        while user1 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user1 = input('\nRock paper scissors says shoot! ')

        while user2 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user2 = input('\nRock paper scissors says shoot! ')

        while user3 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user3 = input('\nRock paper scissors says shoot! ')

        game1 = (user1 + ' Vs ' + random.choice([r,p,s])) 
        game2 = (user2 + ' Vs ' + random.choice([r,p,s]))
        game3 = (user3 + ' Vs ' + random.choice([r,p,s]))

        print('\n' + game1 + '               ' + game2 + '               ' + game3)

        #DOUBLE WINS

        if game1 in lost and game2 in win and game3 in win: #lost win win
             print('You Win')
        elif game1 in win and game2 in lost and game3 in win: #win lost win
            print('You Win')
        elif game1 in win and game2 in win and game3 in lost: #win win lost
            print('You Win')

                                                       
        if game1 in tie and game2 in win and game3 in win:  #tie win win
            print('You Win')
        elif game1 in win and game2 in tie and game3 in win: #win tie win
            print('You Win')
        elif game1 in win and game2 in win and game3 in tie:#win win tie 
            print('You Win')

        if game1 in win and game2 in win and game3 in win: #win win win
            print('You Win')

#DOUBLE LOST

                                                      
        if game1 in win and game2 in lost and game3 in lost: #win lost lost  
            print('You Lost')
        elif game1 in lost and game2 in win and game3 in lost: #lost win lost 
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in win: #lost lost win  
            print('You Lost')

                                                  
        if game1 in tie and game2 in lost and game3 in lost: #tie lost lost  
            print('You Lost')
        elif game1 in lost and game2 in tie and game3 in lost: #lost tie lost
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in tie:  #lost lost tie
            print('You Lost')

        if game1 in lost and game2 in lost and game3 in lost: #lost lost lost
            print('You Lost')

#DOUBLE TIE


        if game1 in tie and game2 in tie and game3 in win: #tie tie win 
            print('You Win')
        elif game1 in tie and game2 in tie and game3 in lost: #tie tie lost
            print('You Lost')











    #tie win tie

    while game1 in tie and game2 in win and game3 in tie:
        print('\nIts a tie')
        print('Go again')

        user1 = input('\nRock paper scissors says shoot! ')
        user2 = input('\nRock paper scissors says shoot! ')
        user3 = input('\nRock paper scissors says shoot! ')  
  
     
        while user1 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user1 = input('\nRock paper scissors says shoot! ')

        while user2 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user2 = input('\nRock paper scissors says shoot! ')

        while user3 not in pos1:
            print('Please type a proper answer and please use lower case letters.\n')
            user3 = input('\nRock paper scissors says shoot! ')

        game1 = (user1 + ' Vs ' + random.choice([r,p,s])) 
        game2 = (user2 + ' Vs ' + random.choice([r,p,s]))
        game3 = (user3 + ' Vs ' + random.choice([r,p,s]))

        print('\n' + game1 + '               ' + game2 + '               ' + game3)


      
#DOUBLE WINS

        if game1 in lost and game2 in win and game3 in win: #lost win win
             print('You Win')
        elif game1 in win and game2 in lost and game3 in win: #win lost win
            print('You Win')
        elif game1 in win and game2 in win and game3 in lost: #win win lost
            print('You Win')

                                                       
        if game1 in tie and game2 in win and game3 in win:  #tie win win
            print('You Win')
        elif game1 in win and game2 in tie and game3 in win: #win tie win
            print('You Win')
        elif game1 in win and game2 in win and game3 in tie:#win win tie 
            print('You Win')

        if game1 in win and game2 in win and game3 in win: #win win win
            print('You Win')

#DOUBLE LOST

                                                      
        if game1 in win and game2 in lost and game3 in lost: #win lost lost  
            print('You Lost')
        elif game1 in lost and game2 in win and game3 in lost: #lost win lost 
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in win: #lost lost win  
            print('You Lost')

                                                  
        if game1 in tie and game2 in lost and game3 in lost: #tie lost lost  
            print('You Lost')
        elif game1 in lost and game2 in tie and game3 in lost: #lost tie lost
            print('You Lost')
        elif game1 in lost and game2 in lost and game3 in tie:  #lost lost tie
            print('You Lost')

        if game1 in lost and game2 in lost and game3 in lost: #lost lost lost
            print('You Lost')

#DOUBLE TIE


        if game1 in tie and game2 in tie and game3 in win: #tie tie win 
            print('You Win')
        elif game1 in tie and game2 in tie and game3 in lost: #tie tie lost
            print('You Lost')





    
    


 


    

    

    
 
 
    
 
 
    
