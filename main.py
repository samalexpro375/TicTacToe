from random import randint
from os import system
from time import sleep

game = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 0
bot = 0
chooser = input("Выбирай: x/o: ")
bot_mark = ''

def player_game():
    while True:
        try:
            player = int(input("Выбирай клетку(1-9): "))
            break
        except:
            print("Сейчас по шляпе получишь!")
    if player-1 >= 0 and player-1 < 9 and game[player-1] != 'X' and game[player-1] != 'O':
        game[player-1] = chooser.upper()
    elif player == 908:
        exit(0)
    else:
        print("Сейчас по шляпе получишь!")
        player_game()

def bot_game():
    while True:
        bot = randint(0, 8)
        if game[bot] != 'X' and game[bot] != 'O':
            game[bot] = bot_mark.upper()
            break
def check_winner():
    if (game[0] == game[1] == game[2] and game[0] != ' ') and (game[1] != ' ' and game[2] != ' '):
        print(f"Победитель: {game[0]}")
        sleep(5)
        exit(0)
    elif (game[3] == game[4] == game[5]) and (game[3] != ' ' and game[4] != ' ' and game[5] != ' '):
        print(f"Победитель: {game[3]}")
        sleep(5)
        exit(0)
    elif (game[6] == game[7] == game[8]) and (game[6] != ' ' and game[7] != ' ' and game[8] != ' '):
        print(f"Победитель: {game[6]}")
        sleep(5)
        exit(0)
    elif (game[0] == game[3] == game[6]) and (game[0] != ' ' and game[3] != ' ' and game[6] != ' '):
        print(f"Победитель: {game[3]}")
        sleep(5)
        exit(0)
    elif (game[1] == game[4] == game[7]) and (game[1] != ' ' and game[4] != ' ' and game[7] != ' '):
        print(f"Победитель: {game[1]}")
        sleep(5)
        exit(0)
    elif (game[2] == game[5] == game[8]) and (game[2] != ' ' and game[5] != ' ' and game[8] != ' '):
        print(f"Победитель: {game[2]}")
        sleep(5)
        exit(0)
    elif (game[0] == game[4] == game[8]) and (game[0] != ' ' and game[4] != ' ' and game[8] != ' '):
        print(f"Победитель: {game[0]}")
        sleep(5)
        exit(0)
    elif (game[2] == game[4] == game[6]) and (game[2] != ' ' and game[4] != ' ' and game[6] != ' '):
        print(f"Победитель: {game[2]}")
        sleep(5)
        exit(0)
    
system('clear')
print(f"""
                                          
                    #         #        
               {game[0]}    #    {game[1]}    #    {game[2]}
                    #         #        
           #############################
                    #         #        
               {game[3]}    #    {game[4]}    #    {game[5]}
                    #         # 
           #############################
                    #         #
               {game[6]}    #    {game[7]}    #    {game[8]}
                    #         #

      """)
if chooser == 'x' or chooser == 'х':
    bot_mark = 'o'
    while True:
            
        player_game()
        
        system('clear')
        print(f"""
                                          
                    #         #        
               {game[0]}    #    {game[1]}    #    {game[2]}
                    #         #        
           #############################
                    #         #        
               {game[3]}    #    {game[4]}    #    {game[5]}
                    #         # 
           #############################
                    #         #
               {game[6]}    #    {game[7]}    #    {game[8]}
                    #         #

      """)
        counter = 0
        for i in range(9):
            if game[i] == 'O' or game[i] == 'X':
                counter += 1
        if counter == 9:
            check_winner()
            print("Ничья!")
            sleep(5)
            exit(0)
        else:
            check_winner()
        bot_game()
        
        system('clear')
        print(f"""
                                          
                    #         #        
               {game[0]}    #    {game[1]}    #    {game[2]}
                    #         #        
           #############################
                    #         #        
               {game[3]}    #    {game[4]}    #    {game[5]}
                    #         # 
           #############################
                    #         #
               {game[6]}    #    {game[7]}    #    {game[8]}
                    #         #

      """)
        counter = 0
        for i in range(9):
            if game[i] == 'O' or game[i] == 'X':
                counter += 1
        if counter == 9:
            check_winner()
            print("Ничья!")
            sleep(5)
            exit(0)
        else:
            check_winner()
elif chooser == 'o' or chooser == 'о':
    bot_mark = 'x'
    while True:
            
        bot_game()
        
        system('clear')
        print(f"""
                                          
                    #         #        
               {game[0]}    #    {game[1]}    #    {game[2]}
                    #         #        
           #############################
                    #         #        
               {game[3]}    #    {game[4]}    #    {game[5]}
                    #         # 
           #############################
                    #         #
               {game[6]}    #    {game[7]}    #    {game[8]}
                    #         #

      """)
        counter = 0
        for i in range(9):
            if game[i] == 'O' or game[i] == 'X':
                counter += 1
        if counter == 9:
            check_winner()
            print("Ничья!")
            sleep(5)
            exit(0)
        else:
            check_winner()
        player_game()
        
        system('clear')
        print(f"""
                                          
                    #         #        
               {game[0]}    #    {game[1]}    #    {game[2]}
                    #         #        
           #############################
                    #         #        
               {game[3]}    #    {game[4]}    #    {game[5]}
                    #         # 
           #############################
                    #         #
               {game[6]}    #    {game[7]}    #    {game[8]}
                    #         #

      """)
        for i in range(9):
            if game[i] == 'O' or game[i] == 'X':
                counter += 1
        if counter == 9:
            check_winner()
            print("Ничья!")
            sleep(5)
            exit(0)
        else:
            check_winner()
else:
    print("Так низя!")

