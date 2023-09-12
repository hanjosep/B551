# a2
#### by: Josep Han (hanjos), Tarini Dash (tdash), Tyler Goblirsch (tygoblir)
#### 11/1/2020

### Part 1: Game of Sebastian
This problem was reminiscent of how we approached the practice dice assignment: rolling a certain amount of dice, and determining which expected value of each reroll configuration.\
We approached this with the conventional expectimax algorithm:\
For each of the configuration of rerolls (e.g. (True, True, True, True, True) for rerolling 5 dice), we look through all of the possible successors of that reroll (e.g. 1,2,3,4,5, or 6) with the other dice that were not rerolled, and then calculate the expected value for each of that configuration. We compare with all of the other configuration's expected values, and then return the highest possible value.\
We started with (False,False,False,False,False) since it's assuming that there is no reroll, but there is no actual benefit since the program iterates through all of the combinations anyways.\
#### Problems Faced/Solutions
One problem we faced was that none of our rolls ran into the bonus flag, so we realized that there could be something we could change in the scoring algorithm. 
* One improvement that we made was to consider the bonus problem: if the bonus flag has not been met yet, we increase the value of having a quartus, quintus, or sextus by 10. This is in attempt to address the fact that getting the bonus would get 35 more points, so these rolls should have a higher value.\
Another problem: In the case where the rerolls returned 0, we at first chose randomly which category to fill.
* The improvement we made here: We compiled an ordered list of the least to most valuable categories relative to their probability, and then we picked the earliest category that remains in the scorecard. This prevented the game from filling valuable categories when it was more probable to occur within the 13 rounds.

### Part 2: Game of Betsy
* The game was played in a 2-D board, so we created an enviroment such that the incoming string was converted into a board (aka a list of rows that includes a list of columns). This allowed us to instantiate a location in the board using board[row][column].
* Next we created a function which calculated the list of successors depending on which side was being played. If it was white's turn, then we compile a list of possible moves that each of white's pieces can go, and then return the list of next possible states out of those possible moves.
* We also generated a heuristic function for the given board. It is very simple, as it compares the white's pieces to the black's; the values are as follows: 
    piece_values = {'R':5, 'N':3.05, 'B':3.33, 'Q':9.5,'K':1000, 'P':1}
* We then approached the Alpha-beta algorithm, which is a subset of the minimax algorithm. This returns the best move for the selected player. 
* Since there is a certain time limit, we modified the alpha-beta program such that their currently explored nodes returned their heuristic values. 

#### Problems faced/Solutions
The main problem was that, although alpha-beta helped prune and reduce the time complexity, it still has a problem that it is by nature depth-first search; if the program gets cut off by time for some reason, it becomes more likely that not all of the lower branches are fully discovered.
* A rough solution we came up was to time a midgame board of betsy, incrementally increase the depth, and compare the time it takes for the alpha-beta pruning to finish. We found that depth 4 was the highest it could go to explore all of the immediate branches and the leaf nodes within the time limit. 
Another problem was that the alpha-beta program returned a None-state board. 
* Looking into it, we realized that the heuristic function originally returned -infinity or infinity if the king was not on the board, indicating a terminal state. Since Betsy does not have checks, we had to get rid of this terminal state and instead have a high value for the kings.