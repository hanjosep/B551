# Automatic Sebastian game player
# B551 Fall 2020
# Based on skeleton code by D. Crandall
#
# This is just a driver program. 
# copy of sebastian.py but with lower total game count to save computation
#

from SebastianState import Dice
from SebastianState import Scorecard
from SebastianAutoPlayer import SebastianAutoPlayer
import time
#######
# Main program:
#
# Plays 100 games of Sebastian and averages together the scores.
#

scores = []
start = time.time()
l = 100
bonuscount = 0
for i in range(0,l):
    print("\n\n***** Starting a new game of Sebastian!!")
    d = Dice()
    s = Scorecard()
    ap = SebastianAutoPlayer()

    for i in range(1, 14):
        print("\n * Turn " + str(i))

        # first roll
        d.roll()
        print("   Roll #1: " + str(d))
        which_to_reroll = ap.first_roll(d, s)

        d.reroll(which_to_reroll)
        print("   Roll #2: " + str(d))
        which_to_reroll = ap.second_roll(d, s)
        
        d.reroll(which_to_reroll)
        print("   Roll #3: " + str(d))
        category = ap.third_roll(d, s)

        s.record(category, d)
        print(s)

    print("Final score: " + str(s.totalscore))
    scores += [s.totalscore,]
    if s.bonusscore == 35:
        bonuscount += 1

print("Min/max/mean scores: " + str(min(scores)) + " " + str(max(scores)) + " " + str(sum(scores)/l))
end = time.time()
print(end-start)
print(bonuscount)