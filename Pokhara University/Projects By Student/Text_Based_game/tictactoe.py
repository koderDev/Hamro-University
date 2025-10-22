def print_board(board):
    print("\n")
        print(" " + board[0] + " | " + board[1] + " | " + board[2])
            print("---+---+---")
                print(" " + board[3] + " | " + board[4] + " | " + board[5])
                    print("---+---+---")
                        print(" " + board[6] + " | " + board[7] + " | " + board[8])
                            print("\n")


                            def check_winner(board, player):
                                # All possible winning combinations
                                    win_conditions = [
                                            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                                                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                                                            (0, 4, 8), (2, 4, 6)              # diagonals
                                                                ]
                                                                    for a, b, c in win_conditions:
                                                                            if board[a] == board[b] == board[c] == player:
                                                                                        return True
                                                                                            return False


                                                                                            def is_full(board):
                                                                                                return " " not in board


                                                                                                def tic_tac_toe():
                                                                                                    board = [" "] * 9
                                                                                                        current_player = "X"

                                                                                                            print("Welcome to Tic Tac Toe!")
                                                                                                                print("Positions are as follows:")
                                                                                                                    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9\n")
                                                                                                                        
                                                                                                                            while True:
                                                                                                                                    print_board(board)
                                                                                                                                            try:
                                                                                                                                                        move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
                                                                                                                                                                    if move < 0 or move > 8:
                                                                                                                                                                                    print("Invalid position! Choose between 1 and 9.")
                                                                                                                                                                                                    continue
                                                                                                                                                                                                                if board[move] != " ":
                                                                                                                                                                                                                                print("That spot is already taken!")
                                                                                                                                                                                                                                                continue
                                                                                                                                                                                                                                                        except ValueError:
                                                                                                                                                                                                                                                                    print("Please enter a number between 1 and 9.")
                                                                                                                                                                                                                                                                                continue

                                                                                                                                                                                                                                                                                        # Make move
                                                                                                                                                                                                                                                                                                board[move] = current_player

                                                                                                                                                                                                                                                                                                        # Check for winner
                                                                                                                                                                                                                                                                                                                if check_winner(board, current_player):
                                                                                                                                                                                                                                                                                                                            print_board(board)
                                                                                                                                                                                                                                                                                                                                        print(f"🎉 Player {current_player} wins! 🎉")
                                                                                                                                                                                                                                                                                                                                                    break

                                                                                                                                                                                                                                                                                                                                                            # Check for draw
                                                                                                                                                                                                                                                                                                                                                                    if is_full(board):
                                                                                                                                                                                                                                                                                                                                                                                print_board(board)
                                                                                                                                                                                                                                                                                                                                                                                            print("It's a draw!")
                                                                                                                                                                                                                                                                                                                                                                                                        break

                                                                                                                                                                                                                                                                                                                                                                                                                # Switch player
                                                                                                                                                                                                                                                                                                                                                                                                                        current_player = "O" if current_player == "X" else "X"


                                                                                                                                                                                                                                                                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                                            tic_tac_toe()