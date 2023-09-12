A1
by: Josep Han (hanjos), Tarini Dash (tdash), Tyler Goblirsch (tygoblir)
Problem 3:
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
•	t = total number of teams or len(current teams)
•	k = user input for time to grade each teams assignment
•	g = complaints due to groupsize
•	r = complaints due to partner requests being ignored
•	n = user input for time to deal with partner request being ignored
•	h = complaints due to partner denials being ignored
•	m = user input for time to deal with partner denials being ignored
In order to quantify g, r, and h we stored input file requests in dictionaries and ran imbedded for loops to add to the count of each wherever the current teams didn’t adhere to the team members request.
Our successor function started with each person on a team of their own and then at random, attempted to combine two teams. It first checked to see if the teams could be combined (len(team1)+len(team2)<=3). Then it would check if the cost new teams was less than the cost of the old teams. We also added some randomness in this check, similar to a Monte Carlo search, to account for some goal states that were near non ideal states, according to the cost function. We ran the combination loop r times, where r was equal to the amount of users times 3 and returned the final team. We the entire combination 1000 times and output the lowest cost team combination.
Finally, our main function takes in the user inputs for the input file, k, m, and n. Reads the input file and stores each users requests into dictionaries. It then initializes teams where each user is on their own team. Runs the successor function, which returns the lowest cost team combination through 1000 iterations. We then continue to run the successor 75 times, only outputting a solution if the cost of the new solution is less than the previous one.
We've assumed for this search function that the amount of users is less than 75, as the settings for how many times the successor function gets run can complete the whole program in around a minute for 75 users. If the user list was larger we would need to bring down the amount of iterations of the successor function in order to run the whole program through.