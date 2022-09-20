# W02 Prove: Developer - Solo Code
# by Zachary Lindstrom
# 2022.09.19 | CSE210-09 | Fall 2022
# https://byui-cse.github.io/cse210-course-competency/introduction/ponder-and-prove.html

# Tic-Tac-Toe Game

# initialize x/o array to store tic-tac-toe location variables
placeholder = [1,2,3,4,5,6,7,8,9]

def main():
    # print initial grid output
    print_grid(placeholder)
    print()

    # while loop to iterate through turns in the game (9 turns maximum)
    i = 1
    while i < 10:
        # this while loop ensures the user doesn't choose a location that's already taken or a number not 1-9
        error = 0
        while error != 1:
            # if statement to check for who's turn it is (x goes first)
            if (i % 2) == 0:    # Player One = x
                team = 'o'
                choice = int(input(f'{team}\'s turn to choose a square (1-9): '))
            else:               # Player Two = o
                team = 'x'
                choice = int(input(f'{team}\'s turn to choose a square (1-9): '))
            
            # error check for if a number isn't 1-9 or if a location is already taken with an x/o
            if choice >= 1 and choice <= 9:
                current_value = placeholder[choice - 1]
                if type(current_value) == int or type(current_value) == float:
                    error = 1
                else:
                    print('I\'m sorry, the current location has already been chosen.')
                    print('Please choose a different location.')
                    print()
            else:
                print('I\'m sorry, your selection is invalid.')
                print('Please choose a location 1-9.')
                print()
        
        # store user choice in the grid and print to terminal
        placeholder[choice - 1] = team
        print_grid(placeholder)
        print()

        # call function to check for a win condition
        win_condition = check_win(placeholder, team)
        if win_condition == 'win':
            print(f'Team {team} Wins!')
            print('Thanks for playing!')
            print()
            i = 10          # ensures the while loop exit
        else:
            if i == 9:
                print('The game is a draw!')
                print('Thanks for playing!')
                print()
                i = 10      # ensures the while loop exit
        
        # increase while loop counter
        i += 1

# this function prints the current grid
def print_grid(placeholder):
    print(f'{placeholder[0]} | {placeholder[1]} | {placeholder[2]}')
    print('- + - + -')
    print(f'{placeholder[3]} | {placeholder[4]} | {placeholder[5]}')
    print('- + - + -')
    print(f'{placeholder[6]} | {placeholder[7]} | {placeholder[8]}')

# this function checks to see if there's a win condition
def check_win(placeholder, team):
    if placeholder[0] == team:
        if placeholder[1] == team:
            if placeholder[2] == team:
                return 'win'
    if placeholder[3] == team:
        if placeholder[4] == team:
            if placeholder[5] == team:
                return 'win'
    if placeholder[6] == team:
        if placeholder[7] == team:
            if placeholder[8] == team:
                return 'win'
    if placeholder[0] == team:
        if placeholder[3] == team:
            if placeholder[6] == team:
                return 'win'
    if placeholder[1] == team:
        if placeholder[4] == team:
            if placeholder[7] == team:
                return 'win'
    if placeholder[2] == team:
        if placeholder[5] == team:
            if placeholder[8] == team:
                return 'win'
    if placeholder[0] == team:
        if placeholder[4] == team:
            if placeholder[8] == team:
                return 'win'
    if placeholder[2] == team:
        if placeholder[4] == team:
            if placeholder[6] == team:
                return 'win'

# Call main to start this program.
if __name__ == "__main__":
    main()
