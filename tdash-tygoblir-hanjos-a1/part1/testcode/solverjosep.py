#!/usr/local/bin/python3
# solver20.py : 2020 Sliding tile puzzle solver
#
# Code by: Josep Han (hanjos), Tarini Dash (tdash), Tyler Goblir (tygoblir)
#
# Based on skeleton code by D. Crandall, September 2020
#
from queue import PriorityQueue
import sys

MOVES = { "R": (0, -1), "L": (0, 1), "D": (-1, 0), "U": (1,0) }
ROWS = 4
COLS = 5

def valid_index(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS

# shift a specified row left (1) or right (-1)
def shift_row(state, row, dir):
    change_row = state[(row*COLS):(row*COLS+COLS)]
    # print(change_row)
    return ( state[:(row*COLS)] 
    + change_row[-dir:] 
    + change_row[:-dir] 
    + state[(row*COLS+COLS):], ("L" if dir == -1 else "R") + str(row+1) )

# shift a specified col up (1) or down (-1)
def shift_col(state, col, dir):
    change_col = state[col::COLS]
    s = list(state)
    s[col::COLS] = change_col[-dir:] + change_col[:-dir]
    return (tuple(s), ("U" if dir == -1 else "D") + str(col+1) )

def printable_board(board):
    return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]

# return a list of possible successor states
def successors(state):
    return [ (shift_row(state, row, dir)) for dir in (-1,1) for row in range(0, ROWS) ] + \
        [ (shift_col(state, col, dir)) for dir in (-1,1) for col in range(0, COLS) ]

# check if we've reached the goal
def is_goal(state):
    return sorted(state[:-1]) == list(state[:-1]) 
    
# The solver! - using BFS right now
def solve(initial_board):
    fringe = [ (initial_board, []) ]
    while len(fringe) > 0:
        (state, route_so_far) = fringe.pop()
        for (succ, move) in successors( state ):
            if is_goal(succ):
                return( route_so_far + [move,] )
            fringe.insert(0, (succ, route_so_far + [move,] ) )
    return False

# my implementation (josep han)
# raw number -> pair of row,column coordinates.
def coordify2(num):
    r = int(num/5)
    c = num - (r *5)
    # result.append((r,c))
    return (r,c)
# wrapped_distance: number, goal, length of side -> (int) minimum distance. Helper function.
# a, b wraps the index either over or under its intended limit 
# (input rc depends on whether you want to compare row or column), then checks which way returns the minimum.
def wrapped_distance(num, goal, rc):
    # num -= 1
    a = num + rc
    b = num - rc
    adist = a - goal
    bdist = abs(b -goal )
    cdist = abs(num - goal )
    return min([adist,bdist,cdist]) 

# state_heuristic: given a list of unorganized tiles, returns a sum of
# modified Manhattan distances of all tiles; 
# Modified Manhattan: considers instance of wrap around. 
# since every turn the value of the Modified Manhattan distance changes by 5 when shifting row and 4 when shifting column,
# we will divide the count by their respective values in order to keep the heuristic admissible.
def state_heuristic(state):
    result = []
    rowsum,colsum =(0,0)
    for i in range(len(state)):
        it = state[i]
        # val = the current value in the list.
        # goal = what the value should be. compare the coordinates of these two numbers
        val = coordify2(it - 1)
        goal = coordify2(i)
        row_dist = wrapped_distance(val[0],goal[0], 4)
        col_dist = wrapped_distance(val[1],goal[1], 5)
        rowsum += row_dist
        colsum += col_dist
        result.append((row_dist, col_dist))
    return (rowsum/4) + (colsum/5)

import time
time.time()
# solve2(state) -> list of moves needed to get to organized board.
# this one utilizes a priority queue that follows the m 
def solve2(initial_board):
    fringe = PriorityQueue()
    initheur = state_heuristic(initial_board)
    fringe.put((initheur, (initial_board, [])))
    visited = [initial_board]
    start = time.time()
    # print(fringe)
    icounter = 0
    while not fringe.empty():
        end = time.time()
        got = fringe.get()
        # print('got',got)
        (state, route_so_far) = got[1]
        # icounter = cost function. goes up by 1 every time fringe is popped.
        # Not necessary for calculating heuristics, but as benchmark for time constraints
        icounter += 1
        # print(icounter)
        # initheur = got[0]
        # print(successors(state))
        for (succ,move) in successors(state):
            # print(move) 
            # print_theboard(succ)
            # print('\n')
            # heuristic_of_succ: calculate heuristic of the each successor from the popped fringe.
            heuristic_of_succ = state_heuristic(succ)
            # print(heuristic_of_succ)
            if is_goal(succ):
                # print(end-start, icounter)
                # print(len(route_so_far) +1)
                return(route_so_far + [move,])
            if end - start  > 50:
                # print("passed 30")
                return False, got
            # if succ not in visited:
                # icounter -= 1
            visited.append(succ)
            tt = (list(succ), route_so_far+[move,])
            # print((heuristic_of_succ,tt))
            # fringe is updated with h(s) + c(s), and (successor state, route_so_far).
            # c(s) is length of route so far; additional move included.
            fringe.put((len(route_so_far)+ 1 + heuristic_of_succ, tt))
start_state = []

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve2(tuple(start_state))
    
    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))


