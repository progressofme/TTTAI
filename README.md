# About The AI's

There are currently 11 Tic Tac Toe AI's.

Each one of them has it's flaws, and advantages.

# Creating An AI
Creating an AI for Tic-Tac-Toe involves defining a Python module with a get_move(board) function that returns the row and column where the AI player wants to place its move. The AI module should interact with the main script, which handles the game logic and flow.

Below is a step-by-step guide on how to create an AI for the Tic-Tac-Toe game:

Create a New AI File:
Start by creating a new Python file for your AI. For example, you can create a file named "my_ai.py".

Define the AI Function:
In the "my_ai.py" file, define the get_move(board) function. This function will take the current state of the game board as input and return the AI's desired move in the form of (row, col).

Import Necessary Functions:
In the AI function, you may need to import functions from the main script to access the game board, check for a winner, etc. Make sure to import any required functions, like check_winner(board, player).

Implement the AI Logic:
Inside the get_move(board) function, implement the AI logic for making a move. This logic can be as simple as choosing a random empty cell or using a more advanced algorithm like the minimax algorithm to find the best move.

Handle Invalid Moves (Optional):
You can add logic to handle cases where the AI selects an invalid move, like choosing a cell that is already occupied.

Testing the AI:
Before using the AI in the main script, it's a good idea to test the AI function separately to ensure it behaves as expected. This can be done by running it through the python file.

Repeat and Improve:
After you see it on Twitch/Youtube (if it gets accepted), You can see what you can improve on. There's always room for improvement!

For more complex games, you may need more sophisticated algorithms and approaches.
