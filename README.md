# About The AI's

There are currently 11 Tic Tac Toe AI's.

# Bad / Random AI's:

BadAI - All of it's moves are random

WorstAI - Only takes the edge moves, all random.

ImpossibleAI - Sees a loss in one move, and prevents it. All other moves are random.

MateInOne - All moves are random except for when it sees a win in one move for themselves.

# Eh AI's:

Intermediate - It's okay. Not much else to say.

Champion - Combined code of every AI. Not that good.

Best - Not the best. It makes good moves but misses wins in one for the other team. Named after Chess.

Torch - Takes the longest to start up, and it only eh. 

# Best AI's:

Boredom - One of the best! It either wins or ties with the top AI's

Fishstock - It took the code from MateInOne, ImpossibleAI, and Best to make the top AI right now. Named after Stockfish for Chess.

Fascination - The best AI right now. Beats Boredom, knows stratigies, and beats some humans. Named after boredom, being the opposite.


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
After you see it on Twitch (if it gets accepted), You can see what you can improve on. There's always room for improvement!

Remember that Tic-Tac-Toe is a relatively simple game, so even basic AI strategies can perform well. For more complex games, you may need more sophisticated algorithms and approaches.

Once you've created your AI, you can compare its performance against other AIs in the Tic-Tac-Toe game and further refine it based on the outcomes. Have fun experimenting and building smarter AIs!
