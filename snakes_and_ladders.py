"""
File: snakes_and_ladders.py
-----------------------------
This is a two player snakes and ladders game.
One who reaches to 100 first, overcoming all the snakes
and taking help from the ladders wins the game.
"""
import random
from colorama import init
from termcolor import colored
init()

# SNAKES:
SNAKE_MOUTH_1 = 12
SNAKE_TAIL_END_1 = 7
SNAKE_MOUTH_2 = 19
SNAKE_TAIL_END_2 = 1
SNAKE_MOUTH_3 = 24
SNAKE_TAIL_END_3 = 15
SNAKE_MOUTH_4 = 38
SNAKE_TAIL_END_4 = 22
SNAKE_MOUTH_5 = 56
SNAKE_TAIL_END_5 = 34
SNAKE_MOUTH_6 = 72
SNAKE_TAIL_END_6 = 47
SNAKE_MOUTH_7 = 90
SNAKE_TAIL_END_7 = 50
SNAKE_MOUTH_8 = 94
SNAKE_TAIL_END_8 = 85
SNAKE_MOUTH_9 = 96
SNAKE_TAIL_END_9 = 79
SNAKE_MOUTH_10 = 99
SNAKE_TAIL_END_10 = 3

# LADDERS:
LADDER_STARTING_1 = 8
LADDER_ENDING_1 = 27
LADDER_STARTING_2 = 14
LADDER_ENDING_2 = 36
LADDER_STARTING_3 = 49
LADDER_ENDING_3 = 93
LADDER_STARTING_4 = 56
LADDER_ENDING_4 = 83
LADDER_STARTING_5 = 77
LADDER_ENDING_5 = 95
LADDER_STARTING_6 = 82
LADDER_ENDING_6 = 97


def main():
    # players = int(input("Enter number of players: "))
    # if players == 2:
    two_players()


def two_players():
    token_1 = 0
    token_2 = 0
    x = both_not_started()
    if x == 1:
        token_1, token_2 = only_player_1_started(token_1, token_2)
        both_started(token_1, token_2)
    elif x == 2:
        token_1, token_2 = only_player_2_started(token_1, token_2)
        '''
        As the only_player_2_started function finishes at a point where player 1 has completed  
        its turn and now its the turn of player 2. But the both_started function starts with 
        player 1's turn. So to avoid player 1 to take 2 turns we manually made player 2 to take turn.
        '''
        die_2 = roll_die_player_2()
        token_2 = move_token_based_on_die_num(token_2, die_2)
        token_2 = bitten_climbed(token_2)
        print(colored('Player 2 is at ' + str(token_2), 'green', attrs=['bold']))
        print('')
        both_started(token_1, token_2)


# Function ends if any one of the two players gets a 6 on rolling the die.
# Returns 1 if player 1 first gets a 6 on rolling the die.
# Returns 2 if player 2 first gets a 6 on rolling the die.
def both_not_started():
    while True:
        die_1 = need_6_player_1()
        if die_1 == 6:
            print(colored("Player 1 has started.", 'red', attrs=['bold']))
            return 1
        die_2 = need_6_player_2()
        if die_2 == 6:
            print(colored("Player 2 has started.", 'green', attrs=['bold']))
            return 2


def only_player_1_started(token_1, token_2):
    while True:
        die_1 = roll_die_player_1()
        token_1 = move_token_based_on_die_num(token_1, die_1)
        token_1 = bitten_climbed(token_1)
        print(colored('Player 1 is at ' + str(token_1), 'red', attrs=['bold']))
        print('')
        die_2 = need_6_player_2()
        if die_2 == 6:
            print(colored("Player 2 has started.", 'green', attrs=['bold']))
            # After starting, the same player gets a turn to again roll the die and move the token.
            die_2 = roll_die_player_2()
            token_2 = move_token_based_on_die_num(token_2, die_2)
            token_2 = bitten_climbed(token_2)
            print(colored('Player 2 is at ' + str(token_2), 'green', attrs=['bold']))
            print('')
            break
    return token_1, token_2


def only_player_2_started(token_1, token_2):
    while 1:
        die_2 = roll_die_player_2()
        token_2 = move_token_based_on_die_num(token_2, die_2)
        token_2 = bitten_climbed(token_2)
        print(colored('Player 2 is at ' + str(token_2), 'green', attrs=['bold']))
        print('')
        die_1 = need_6_player_1()
        if die_1 == 6:
            print(colored("Player 1 has started.", 'red', attrs=['bold']))
            # After starting, the same player gets a turn to again roll the die and move the token.
            die_1 = roll_die_player_1()
            token_1 = move_token_based_on_die_num(token_1, die_1)
            token_1 = bitten_climbed(token_1)
            print(colored('Player 1 is at ' + str(token_1), 'red', attrs=['bold']))
            print('')
            break
    return token_1, token_2


def both_started(token_1, token_2):
    while (token_1 < 100) and (token_2 < 100):
        die_1 = roll_die_player_1()
        token_1 = move_token_based_on_die_num(token_1, die_1)
        token_1 = bitten_climbed(token_1)
        if token_1 <= 100:
            print(colored('Player 1 is at ' + str(token_1), 'red', attrs=['bold']))
            print('')
        if token_1 >= 100:
            print('')
            print(colored("Player 1 is the winner!!", 'yellow', 'on_red', attrs=['bold']))
            break
        die_2 = roll_die_player_2()
        token_2 = move_token_based_on_die_num(token_2, die_2)
        token_2 = bitten_climbed(token_2)
        if token_2 <= 100:
            print(colored('Player 2 is at ' + str(token_2), 'green', attrs=['bold']))
            print('')
        if token_2 >= 100:
            print('')
            print(colored("Player 2 is the winner!!", 'yellow', 'on_red', attrs=['bold']))
            break


def roll_die_player_1():
    roll = input(colored("Player 1 enter R or r for rolling a die: ", 'red'))
    # if the user input is R or r only then roll die.
    if roll.upper() == 'R':
        die_1 = random.randint(1, 6)
        print(colored("Die showed: " + str(die_1), 'red'))
    # Otherwise prompt please input r ot r.
    # If the input is R or r then roll die otherwise keep on prompting please input R ot r.
    else:
        while roll.upper() != 'R':
            roll = input(colored('Please enter R ot r: ', 'red'))
        die_1 = random.randint(1, 6)
        print(colored("Die showed: " + str(die_1), 'red'))
    return die_1


def roll_die_player_2():
    roll = input(colored("Player 2 enter R or r for rolling a die: ", 'green'))
    if roll.upper() == 'R':
        die_2 = random.randint(1, 6)
        print(colored("Die showed: " + str(die_2), 'green'))
    else:
        while roll.upper() != 'R':
            roll = input(colored('Please enter R ot r: ', 'green'))
        die_2 = random.randint(1, 6)
        print(colored("Die showed: " + str(die_2), 'green'))
    return die_2


def need_6_player_1():
    roll = input(colored("Player 1 enter R or r for rolling a die: ", 'red'))
    if roll.upper() == 'R':
        die_1 = random.randint(1, 6)
        print(colored("Die showed: " + str(die_1), 'red'))
        if die_1 != 6:
            print(colored('You need 6 to start.', 'red', attrs=['bold']))
            print('')
    else:
        while roll.upper() != 'R':
            roll = input(colored('Please enter R ot r: ', 'red'))
        die_1 = random.randint(1, 6)
        print(colored("Die showed: " + str(die_1), 'red'))
        if die_1 != 6:
            print(colored('You need 6 to start.', 'red', attrs=['bold']))
            print('')
    return die_1


def need_6_player_2():
    roll = input(colored("Player 2 enter R or r for rolling a die: ", 'green'))
    if roll.upper() == 'R':
        die_2 = random.randint(1, 6)
        print(colored("Die showed: " + str(die_2), 'green'))
        if die_2 != 6:
            print(colored('You need 6 to start.', 'green', attrs=['bold']))
            print('')
    else:
        while roll.upper() != 'R':
            roll = input(colored('Please enter R ot r: ', 'green'))
        die_2 = random.randint(1, 6)
        print(colored("Die showed: " + str(die_2), 'green'))
        if die_2 != 6:
            print(colored('You need 6 to start.', 'green', attrs=['bold']))
            print('')
    return die_2


def move_token_based_on_die_num(current_location, die_showed):
    a = current_location + die_showed
    if a <= 100:
        current_location += die_showed
    else:
        print(colored('You need ' + str(100 - current_location) + ' to win', 'blue', attrs=['bold']))
    return current_location


def bitten_climbed(current_location):
    # If the token gets bitten by the snake then move the token to the end of the tail of the snake.
    if current_location == SNAKE_MOUTH_1:
        print(colored("You are bitten by a snake!!", 'blue', attrs=['bold']))
        current_location = int(SNAKE_TAIL_END_1)
    elif current_location == SNAKE_MOUTH_2:
        print(colored("You are bitten by a snake!!", 'blue', attrs=['bold']))
        current_location = int(SNAKE_TAIL_END_2)
    elif current_location == SNAKE_MOUTH_3:
        print(colored("You are bitten by a snake!!", 'blue', attrs=['bold']))
        current_location = int(SNAKE_TAIL_END_3)
    elif current_location == SNAKE_MOUTH_4:
        print(colored("You are bitten by a snake!!", 'blue', attrs=['bold']))
        current_location = int(SNAKE_TAIL_END_4)
    elif current_location == SNAKE_MOUTH_5:
        print(colored("You are bitten by a snake!!", 'blue', attrs=['bold']))
        current_location = int(SNAKE_TAIL_END_5)
    elif current_location == SNAKE_MOUTH_6:
        print(colored("You are bitten by a snake!!", 'blue', attrs=['bold']))
        current_location = int(SNAKE_TAIL_END_6)
    elif current_location == SNAKE_MOUTH_7:
        print(colored("You are bitten by a snake!!", 'blue', attrs=['bold']))
        current_location = int(SNAKE_TAIL_END_7)
    elif current_location == SNAKE_MOUTH_8:
        print(colored("You are bitten by a snake!!", 'blue', attrs=['bold']))
        current_location = int(SNAKE_TAIL_END_8)
    elif current_location == SNAKE_MOUTH_9:
        print(colored("You are bitten by a snake!!", 'blue', attrs=['bold']))
        current_location = int(SNAKE_TAIL_END_9)
    elif current_location == SNAKE_MOUTH_10:
        print(colored("You are bitten by a snake!!", 'blue', attrs=['bold']))
        current_location = int(SNAKE_TAIL_END_10)

    # If the token climbs a ladder then move the token to the upper end of the ladder
    elif current_location == LADDER_STARTING_1:
        print(colored("You climbed a ladder!!", 'blue', attrs=['bold']))
        current_location = int(LADDER_ENDING_1)
    elif current_location == LADDER_STARTING_2:
        print(colored("You climbed a ladder!!", 'blue', attrs=['bold']))
        current_location = int(LADDER_ENDING_2)
    elif current_location == LADDER_STARTING_3:
        print(colored("You climbed a ladder!!", 'blue', attrs=['bold']))
        current_location = int(LADDER_ENDING_3)
    elif current_location == LADDER_STARTING_4:
        print(colored("You climbed a ladder!!", 'blue', attrs=['bold']))
        current_location = int(LADDER_ENDING_4)
    elif current_location == LADDER_STARTING_5:
        print(colored("You climbed a ladder!!", 'blue', attrs=['bold']))
        current_location = int(LADDER_ENDING_5)
    elif current_location == LADDER_STARTING_6:
        print(colored("You climbed a ladder!!", 'blue', attrs=['bold']))
        current_location = int(LADDER_ENDING_6)
    return current_location


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()