# Automatic Sebastian game player
# B551 Fall 2020
# Josep Han, Tarini Dash, Tyler Goblirsch
# hanjos, tdash, tygoblir
#
# Based on skeleton code by D. Crandall
#
#
# This is the file you should modify to create your new smart player.
# The main program calls this program three times for each turn. 
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list 
#      of dice indices that should be re-rolled.
#   
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that 
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#

from SebastianState import Dice
from SebastianState import Scorecard
import random

class SebastianAutoPlayer:

      def __init__(self):
            choices=  [True,False]
            somelist = [(a,b,c,d,e) for a in choices for b in choices for c in choices for d in choices for e in choices]
            # pass  
      # def evaluate_dice(self,dice,scoreboard):
      def highest_score(self, scorecard):
            og = list(set(Scorecard.Categories))
            ca = list(set(Scorecard.Categories) - set(scorecard.scorecard.keys()))
            # for cat in ca: 
            #       if cat == '':
      def least_valuable(self,scorecard):
            least_likely = ['primis','secundus', 'tertium', 'quartus', 'quadrupla', 'quintus', 'quintuplicatam', 'sextus', 'triplex',
 'pandemonium', 'squadron', 'prattle', 'company']
            for item in least_likely:
                  if item in list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())):
                        return item

      def heuristic(self,dice,scorecard):
            # go over all of the scorecard's available options and pick the highest value
            # print('you')
            
            # print(list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())))
            # print(scorecard.record(random.choice(list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())))))
            # print(dice)

            counts = [dice.count(i) for i in range(1,7)]
            maxscore = (0,'')
            for category in list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())):
                  score = 0
                  if category in Scorecard.Numbers:
                        if category in ['sextus','quintus','quartus'] and scorecard.bonusscore == 0:
                              score = counts[Scorecard.Numbers[category]-1] * Scorecard.Numbers[category] + 10
                        else:
                              score = counts[Scorecard.Numbers[category]-1] * Scorecard.Numbers[category]
                  elif category == "company":
                        score = 40 if sorted(dice) == [1,2,3,4,5] or sorted(dice) == [2,3,4,5,6] else 0
                  elif category == "prattle":
                        score = 30 if (len(set([1,2,3,4]) - set(dice)) == 0 or len(set([2,3,4,5]) - set(dice)) == 0 or len(set([3,4,5,6]) - set(dice)) == 0) else 0
                  elif category == "squadron":
                        score = 25 if (2 in counts) and (3 in counts) else 0
                  elif category == "triplex":
                        score = sum(dice) if max(counts) >= 3 else 0
                  elif category == "quadrupla":
                        score = sum(dice) if max(counts) >= 4 else 0
                  elif category == "quintuplicatam":
                        score = 50 if max(counts) == 5 else 0
                  elif category == "pandemonium":
                        score = sum(dice)
                  else:
                        print("Error: unknown category")
                  if score > maxscore[0]:
                        maxscore = (score,category)
            # print(maxscore)
            if maxscore[0] == 0:
                  # ranchoice = random.choice(list(set(Scorecard.Categories) - set(scorecard.scorecard.keys()))) 
                  unlikely = self.least_valuable(scorecard)
                  # print(ranchoice)
                  return (0, unlikely)

            else:
                  # print(maxscore)
                  return maxscore
      def expectation_of_reroll(self,roll,reroll,scorecard):
            exp = 0
            outcome_count = 0
            for outcome_a in (roll[0],) if not reroll[0] else range(1,7):
                  for outcome_b in (roll[1],) if not reroll[1] else range(1,7):
                        for outcome_c in (roll[2],) if not reroll[2] else range(1,7):
                              for outcome_d in (roll[3],) if not reroll[3] else range(1,7):
                                    for outcome_e in (roll[4],) if not reroll[4] else range(1,7):
                                          var = [outcome_a,outcome_b,outcome_c,outcome_d,outcome_e]
                                          h = self.heuristic(var, scorecard)
                                          # print(h)
                                          exp += h[0]

                                          outcome_count += 1
            return exp * 1.0 / outcome_count

      def max_layer(self, roll,scorecard):
            max_so_far = (0,0)
            # print(roll)
            for roll_a in (False, True):
                  for roll_b in (False, True):
                        for roll_c in (False, True):
                              for roll_d in (False, True):
                                    for roll_e in (False, True):
                                          this_reroll = (roll_a,roll_b,roll_c,roll_d,roll_e)
                                          exp_score = self.expectation_of_reroll(roll,this_reroll,scorecard)

                                          # print(this_reroll,exp_score)
                                          if exp_score > max_so_far[1]:
                                                max_so_far = (this_reroll, exp_score)
                                          if max_so_far[1] > 33:
                                                return max_so_far
            return max_so_far
      def chosse(self, order):
            return [i for i in range(0,len(order[0])) if order[0][i] == True]

      def first_roll(self, dice, scorecard):
            # print(dice.dice)
            maxh = self.max_layer(dice.dice,scorecard)
            chose = self.chosse(maxh)
            return chose
            # self.heuristic(dice,scorecard)
            # # print('ha!', scorecard)
            # return [0] # always re-roll first die (blindly)

      def second_roll(self, dice, scorecard):
            maxh = self.max_layer(dice.dice,scorecard)
            # print(maxh)
            chose = self.chosse(maxh)
            # print(chose)
            return chose
            # return [1, 2] # always re-roll second and third dice (blindly)
      
      def third_roll(self, dice, scorecard):
            # stupidly just randomly choose a category to put this in
            # randochoice = random.choice( list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) )
            # print(random.choice( list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) ))
            # return random.choice( list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) )
            # print(sorted(dice))
            # if sorted(dice) == [1,2,3,4,5]:
            #       try:
            #             return 'company'
            #       except:
            # print(randochoice)
            educated_choice = self.heuristic(dice.dice,scorecard)
            # return randochoice
            return educated_choice[1]
            
      