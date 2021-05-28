#!/usr/local/bin/python3
# CSCI B551 Fall 2020
#
# Authors: Jack McShane (jamschan)
#
# based on skeleton code by D. Crandall, 11/2020
#
# ./break_code.py : attack encryption
#


import random
import math
import copy
import sys
import encode



class MarkovChain:
    def __init__(self):
        self.default_val = 0
        self.abet = list(map(chr, range(97,123))) + [' ',]
        self.trans = {letter:{char:self.default_val for char in self.abet} for letter in self.abet }


    def calc_transitions(self, doc):
        self.tally_transitions(doc)
        self.transition_count = len(doc) + 1
        self.word_count = len(doc.split())
        #calculating probabilities
        for start in self.trans:
            for transition in self.trans[start]:
                if start == ' ' or transition == ' ':
                    if self.trans[start][transition] == 0:
                        self.trans[start][transition] = .01/self.word_count
                    else:
                        self.trans[start][transition] /= self.word_count
                else:
                    if self.trans[start][transition] == 0:
                        self.trans[start][transition] = .01/self.transition_count
                    else:
                        self.trans[start][transition] /= self.transition_count


    def tally_transitions(self, doc):
        for i in range(1,len(doc)):
            self.trans[doc[i-1]][doc[i]] += 1
        self.trans[' '][doc[0]] += 1
        self.trans[doc[-1]][' '] += 1


#####################END OF MARKOV CHAIN CLASS



# - rearrangement table is of length 4
# - could break into two more methods
def gen_t():
    abet = list(map(chr, range(97,123)))
    shuffled = list( set( abet ) )
    rplace = {abet[i]:shuffled[i] for i in range(len(abet))}

    rrange = list( set( range(4) ) )
    random.shuffle( rrange )

    return (rplace, rrange)



def mod_sub(table):
    abet = set(list(map(chr, range(97,123))))
    item1, item2 = (abet.pop(), abet.pop())
    table[0][item1], table[0][item2] = table[0][item2], table[0][item1]
    return table


def mod_transl(table):
    num1 = random.randrange(len(table[1]))
    num2 = random.randrange(len(table[1]))
    while num1 == num2:
        num1 = random.randrange(len(table[1]))
        num2 = random.randrange(len(table[1]))
    table[1][num1], table[1][num2] = table[1][num2], table[1][num1]
    return table



def logprob(mc, decrypted):
    eng = 0
    for i in range(1, len(decrypted)):
        prob = math.log( mc.trans[decrypted[i-1]][ decrypted[i]] )
        eng += prob
    eng += math.log( mc.trans[' '][decrypted[0]] )
    eng += math.log( mc.trans[decrypted[-1]][' '] )
    return eng




def metropolis_hastings(mc, doc):
    #initialize randomized T
    t = gen_t()
    #consider starting fresh after k iterations
    for i in range(10000):
        #t = t if (i%2000) != 0 else gen_t()
        if random.randrange(30) < 26:
            tp = mod_sub(copy.deepcopy(t))
        else:
            tp = mod_transl(copy.deepcopy(t))

        logprob_decoded_t = logprob(mc, encode.encode(doc, t[0], t[1]))
        logprob_decoded_tp = logprob(mc, encode.encode(doc, tp[0], tp[1]))

        # logprob is closer to zero if probability is larger
        # check to make sure comparison is right
        if abs(logprob_decoded_tp) < abs(logprob_decoded_t):
            t = copy.deepcopy(tp)
        else:
            ratio = math.exp( logprob_decoded_tp - logprob_decoded_t )
            if random.random() > ratio:
                t = copy.deepcopy(t)
            else:
                t = copy.deepcopy(tp)

    return t





# put your code here!
def break_code(string, corpus):

    mc = MarkovChain()
    mc.calc_transitions(corpus)

    best_tables = (
        metropolis_hastings(mc, string),
        metropolis_hastings(mc, string),
        metropolis_hastings(mc, string),
        metropolis_hastings(mc, string),
        metropolis_hastings(mc, string)
    )



    return "Not implemented yet!"


if __name__== "__main__":
    if(len(sys.argv) != 4):
        raise Exception("usage: ./break_code.py coded-file corpus output-file")

    encoded = encode.read_clean_file(sys.argv[1])
    corpus = encode.read_clean_file(sys.argv[2])
    decoded = break_code(encoded, corpus)

    with open(sys.argv[3], "w") as file:
        print(decoded, file=file)

