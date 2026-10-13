PLAYER = 'X'
AI = 'O'
EMPTY = ' '
board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

def main():
    print_board()

    while True:
        human_move()
        print_board()
        if check_game_over():
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if check_game_over():
            break

def print_board():
    print("-------------")
    for i in range(3):
        print("| ", end="")
        for j in range(3):
            print(f"{board[i][j]} | ", end="")
        print("\n-------------")

def human_move():
    while True:
        try:
            user_input = input("Enter row (1-3) and column (1-3): ").split()
            if len(user_input) != 2:
                print("Invalid input. Enter row and column separated by space.")
                continue
            row = int(user_input[0]) - 1
            col = int(user_input[1]) - 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == EMPTY:
                board[row][col] = PLAYER
                break
            print("Invalid move. Try again.")
        except ValueError:
            print("Please enter valid numbers.")

def ai_move():
    if find_winning_move(AI):
        return

    if find_winning_move(PLAYER):
        return

    if board[1][1] == EMPTY:
        board[1][1] = AI
        return

    sides = [[0,1], [1,0], [1,2], [2,1]]
    for cell in sides:
        if board[cell[0]][cell[1]] == EMPTY:
            board[cell[0]][cell[1]] = AI
            return
            
    corners = [[0,0], [0,2], [2,0], [2,2]]
    for cell in corners:
        if board[cell[0]][cell[1]] == EMPTY:
            board[cell[0]][cell[1]] = AI
            return

def find_winning_move(mark):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = mark
                is_win = check_win(mark)
                board[i][j] = EMPTY
                if is_win:
                    board[i][j] = AI
                    return True
    return False

def check_win(mark):
    for i in range(3):
        if board[i][0] == mark and board[i][1] == mark and board[i][2] == mark:
            return True
        if board[0][i] == mark and board[1][i] == mark and board[2][i] == mark:
            return True
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    return False

def check_game_over():
    if check_win(PLAYER):
        print("You win!")
        return True
    if check_win(AI):
        print("AI wins!")
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    print("It's a draw!")
    return True

if __name__ == "__main__":
    main()
