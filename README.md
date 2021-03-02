# Project_1

This Project_1 Repository contains all of the necessary components to play a cardgame, add a cheating element, and compare the distributions of data over many games.
This game is based on a deck of size n, determined by the player with the -Ncards command. The deck is split between two "players". The script simulates flipping over cards and comparing values.
If player A has a higher value card, they earn a point. This iterates over the total number of cards in each players hand.
We can then play a number of games to obtain a distribution to analyze with CardgameAnalysis.py. The number of games are determined by user input command -Ngames.

Players have the option to cheat with the -gimme command. This allows them to "insert" a number of cards into their own deck that are guaranteed to win.

CardgameSim.py should be used first. It accepts a -h flag for options.

The CardgameAnalysis.py program will accept a -h flag as well. The user will give inputs for the fair game text file, cheater game text file (for comparison), Ncards used, and gimme cheater cards that were used for the cheater game.

Taking these inputs, the user will obtain a plot of two data sets, if both fair and cheater games were input. These also include data such as the average value, standard deviation, and Z test statistic.

For user reference, I have included a writeup, and sample txt files that have been used by the creator.

Enjoy!
