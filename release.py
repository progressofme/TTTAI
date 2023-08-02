import random
import time
import importlib

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def evaluate(board, player):
    pass

def main():
    ai_file = input("Enter the name of the AI file (without .py extension): ")

    try:
        ai_module = importlib.import_module(ai_file)
        ai_function = ai_module.get_move

        # Check if required functions are available in the AI module
        required_functions = ["check_winner", "is_board_full"]
        if not all(hasattr(ai_module, func) for func in required_functions):
            print("Error: AI module is missing required functions.")
            return

        board = [[" " for _ in range(3)] for _ in range(3)]
        players = ["X", "O"]
        player_idx = 0

        print("Running a test game, there will be no winner.")
        print_board(board)

        while True:
            current_player = players[player_idx]
            if is_board_full(board):
                print("The code works! Feel free to send it in to @loop234 on discord for a chance to see it on twitch.")
                break

            if player_idx == 0:
                row, col = random.randint(0, 2), random.randint(0, 2)
                while board[row][col] != " ":
                    row, col = random.randint(0, 2), random.randint(0, 2)
                time.sleep(1)  # Small delay for AI's move
            else:
                try:
                    row, col = ai_function(board)
                    if board[row][col] != " ":
                        print("Script doesn't work for the reason: SPOT_TAKEN")
                        break
                except Exception as e:
                    print(f"Script doesn't work for the reason: {e}")
                    break
                time.sleep(1)  # Small delay for AI's move

            board[row][col] = current_player
            print(f"{current_player} moves to row {row + 1}, col {col + 1}:")
            print_board(board)

            result = evaluate(board, current_player)
            if result is not None:
                if result == 1:
                    print(f"The code works! Feel free to send it in to @loop234 on discord for a chance to see it on twitch.")
                else:
                    print("The code works! Feel free to send it in to @loop234 on discord for a chance to see it on twitch.")
                break

            player_idx = 1 - player_idx

    except ModuleNotFoundError:
        print("Script doesn't work for the reason: LIBRARY_MISSING")

    time.sleep(60)  # Wait for a minute before exiting

if __name__ == "__main__":
    main()
