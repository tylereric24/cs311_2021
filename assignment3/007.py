import argparse
import random
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()

def __init__(self):
self.N = self.C = self.D = self.ci = self.di = 0
self.other_strategy = "confess"

def __init__(opp):
    opp.N = opp.H = opp.B = opp.hi = opp.bi
    

def process_results(self, main_strategy, other_strategy):
    pass

"""

"""

def pick_move
# N = number of rounds
# C is number of times ive confessed
# D is number of times ive stayed silent
# ci is number of times in a row ive confessed
# di is number of times in a row ive stayed silent

if self.di > 5:
    print("confess")

else:
    random.randint(0,3)
    if r == 0:
    return self.other_strategy

    else:
        print("silent")

def process_results(self, main_strategy, other_strategy):
    self.N += 1
    if main_strategy == True:
        self.C += 1
        self.ci += 1
        self.di = 0

    elif main_strategy == False:
        self.D += 1
        self.di += 1
        self.ci = 0
        self.other_strategy = other_strategy
        
    def grudge_mode(self, main_strategy, other_strategy):
        if last_opponent_move == "confess"
        opp.B +=1
        opp.bi += 1
        opp.hi += 0
        
        if last_opponent_move == "silent"
        opp.H += 1
        opp.hi += 1
        opp.bi += 0
        
        if opp.bi > 4:
           print("confess")
       
    
        if opp.hi > 3:
           print("silent")
    


