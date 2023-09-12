# a1
#### by: Josep Han (hanjos), Tarini Dash (tdash), Tyler Goblirsch (tygoblir)
#### 10/8/2020

### Problem 1:
The state space of the 2020 puzzle is all of the valid permutations of a 4 row, 5 column board, which depends on whether it is reachable by a certain combination of the successor function.\
Successor: The board can shift one row or one column by 1 tile, and it causes a "wrap around" where the tile that falls out of the index goes to the index that is missing. Since there are 4 rows and 5 columns with 2 directions each, the successor function will return 18 possible states as a result of shifting.\
Edge weights: The cost of traversing through each move is going to be 1.\
Goal state: the 2020 puzzle where its configuration is ordered from [1,...,20]

Heuristic function: When discussing heuristics of the board, we had to look into the process of each move. We noticed that whenever the board shifted by row, the number of tiles that got moved was 5, and when done by column, the total tile change was 4. We also noticed that the tiles that were one move away from the goal was actually on the far opposite end of the board. Therefore, we decided to implement a modified Manhattan distance heuristic: we create three instances where the input coordinate is decreased by the length of the row/column, increased by its row/column, or kept the same, and then compare those three to the distance to the goal coordinate.

For the final heuristic function, we sum up the row and column modified distances separately, divide the row sum by 4 and column sum by 5, and then return the sum of these two values. This helps keep each valid move in the successor function fall within a value of 1, thus fitting the admissibility criteria (h(s)+g(s)<= h*(s) )

The search algorithm for Problem 1 follows the A* algorithm, where it begins with initializing a priority queue, where it puts the initial configuration with priority value zero. Then, the queue begins a loop that continues while the queue is not empty:
1. Pop the lowest priority of the queue; becomes the fringe.
2. If the fringe is the goal:
    * return the list of moves it has made to get to that configuration.
    * Terminate loop.
3. Else:
    * Every successor states of this fringe will be given its heuristic value, and the successor's direction label appends to the route that has been taken by its fringe node (its route history).
    * Each successor state will be put into the priority queue; the priority of each successor stae is the length of the route taken + the heuristic value of that state.
6. Restart loop.

The biggest challenge of this algorithm was thinking up of an admissible heuristic function for the board. We knew that a Manhattan distance was very close to being a valid heuristic, but we struggled to think up of a way to implement it. We had to convert the board into (row,column) tuples since the board is given as a flat list, then compared the changes made from each valid move of the board. 

In addition, since the search algorithm was A* using Priority queue, we had to ensure that each successor node was keeping track of the total cost of the board. Before this was corrected, the search algorithm would resort back to BFS, and determining where the algorithm went wrong took a long time.

We've assumed this algorithm will work for a 4x5 board, so the modified Manhattan distance will fail on any other type of board; We've also assumed that the input board is a valid configuration; there is no way to check if it has actually come from a given permutations of valid moves.

### Problem 2:

The program follows below validations

1. Checks it can only accepts 4 arguments
2. Checks cost_function which is args 4 can only accept one of the value "segments", "distance", "time", "cycling
3. Checks start_city and end_city cannot be same.

The program follows below steps
1. Create a dictionary from city-gps.txt
2. Create a connection dictionary from road-segments.txt
3. Loads the start_city to fringe which is a priority q with initial results(Using A* Algorithm)
4. pops the city from the fringe
5. checks if the start_city is equals to end_city then return result
6. else calls the successor function and gets all connectivity city  and stores them in priority q with key as f(s)

The challenge in this program is when you reach to a city and that city/jn does not have a gps value.
Total cost fs) = g(s) cost to reach the node + h(s) GPS distance between the successor city and end_city
PS: When successor city do not have a GPS we have assumed h(s) = abs(h(parent_city) - g(s))

g(s) for 
* segments return 0
* distance return distance
* time return distance)/(mph + 5)
* cycling return distance * mph * 0.000001

Total State Space = All valid path between start_city and end_city
Goal State = end_city


### Problem 3:

The state space for the group assign problem is all valid combinations of teams for the given user inputs. A valid team consists of 3 or less people and every user must be on one team. For example, if the input file consists of 6 users, the state space would be all combinations of team breakouts outlined below:
1.	2 teams of 3
2.	1 team of 3, 1 team of 2 and 1 team of 1
3.	1 team of 3, and 3 teams of 1
4.	3 teams of 2
5.	2 teams of 2 and 2 teams of 1
6.	1 team of 2 and 4 teams of 1
7.	6 teams of 1
Because the state space is so large and the path to the solution is unimportant, we decided that a local search was the most feasible way to approach this problem. The process of creating a local search for this problem started with creating a cost function. Our cost function is defined is defined below:
Cost(current teams) = (t*k)+(g) + (r*n) + (h*m)
*	t = total number of teams or len(current teams)
*	k = user input for time to grade each teams assignment
*	g = complaints due to groupsize
*	r = complaints due to partner requests being ignored
*	n = user input for time to deal with partner request being ignored
*	h = complaints due to partner denials being ignored
*	m = user input for time to deal with partner denials being ignored

In order to quantify g, r, and h we stored input file requests in dictionaries and ran imbedded for loops to add to the count of each wherever the current teams didn’t adhere to the team members request.
Our successor function started with each person on a team of their own and then at random, attempted to combine two teams. It first checked to see if the teams could be combined (len(team1)+len(team2)<=3). Then it would check if the cost new teams was less than the cost of the old teams. We also added some randomness in this check, similar to a Monte Carlo search, to account for some goal states that were near non ideal states, according to the cost function. We ran the combination loop r times, where r was equal to the amount of users times 3 and returned the final team. We the entire combination 1000 times and output the lowest cost team combination.\
Finally, our main function takes in the user inputs for the input file, k, m, and n. Reads the input file and stores each users requests into dictionaries. It then initializes teams where each user is on their own team. Runs the successor function, which returns the lowest cost team combination through 1000 iterations. We then continue to run the successor 75 times, only outputting a solution if the cost of the new solution is less than the previous one.\
We've assumed for this search function that the amount of users is less than 75, as the settings for how many times the successor function gets run can complete the whole program in around a minute for 75 users. If the user list was larger we would need to bring down the amount of iterations of the successor function in order to run the whole program through.