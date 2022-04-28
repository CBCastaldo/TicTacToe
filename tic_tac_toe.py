'''
Title: tic_tac_toe.py
Author: Chelsea Castaldo

Purpose: Design a program using the principles of programming with classes.
'''

def main():
    play_again = 'yes'
    while play_again.lower() == 'yes':
        try:
            # count = 0
            player = new_turn('')
            grid = draw_grid()
            while not (winner(grid) or game_is_draw(grid)):
                show_grid(grid)
                choose_square(player, grid)
                player = new_turn(player)
            show_grid(grid)
            print('Good game.')
            print()
            play_again = input('Would you like to play again (yes/no)? ')
            print()
        except ValueError as val_err:
            print('Error:', val_err)
            print('Try Again.')
    else:
        print('Thanks for playing.')
        print()

def draw_grid():
    grid = []
    for square in range(9):
        grid.append(square + 1)
    return grid

def show_grid(grid):
    print()
    print(f'{grid[6]}|{grid[7]}|{grid[8]}')
    print('-+-+-')
    print(f'{grid[3]}|{grid[4]}|{grid[5]}')
    print('-+-+-')
    print(f'{grid[0]}|{grid[1]}|{grid[2]}')
    print()

def new_turn(turn):
    if turn == '' or turn == 'O':
        return 'X'
    elif turn == 'X':
        return 'O'
    
def choose_square(player, grid):
    square = int(input(f'It\'s {player}\'s turn. Make your move (0-9)? '))
    grid[square - 1] = player
    # count = count + 1

def winner(grid):
    return (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6])
    # print(f'{turn} wins!')
    # else:
    #     print('It\'s a draw.')

def game_is_draw(grid):
    for square in range(9):
        if grid[square] != 'X' and grid[square] != 'O':
            return False
    return True

if __name__ == "__main__":
    main()