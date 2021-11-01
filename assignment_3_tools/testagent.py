import argparse
import random
import os
from queue import LifoQueue

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help = 'called when new game')
    parser.add_argument('--iterations', help = 'number of iterations in game')
    parser.add_argument('--last_opponent_move', help = 'last opponent move')

    args = parser.parse_args()
    if args.last_opponent_move == "zero" :
        f = open("grudge.txt", "w")
        grudgecounter = "0.5"
        f.write(grudgecounter)
        print("silent")
        f.close()
        f = open("storage.txt", "w")
        f.write("")
    else :
        stack = LifoQueue(maxsize = 200)
        f = open("storage.txt", "r")
        for x in f :
            stack.put(x)
        f.close()
        f = open("grudge.txt", "r")
        grudgecounter = f.read()
        stack.put(args.last_opponent_move)
        grudgecounter = float(grudgecounter)
        if random.randint(0,10) == 1 :
            grudgecounter = grudgecounter / 1.3
        if args.last_opponent_move == "confess" :
            grudgecounter += 4
        if grudgecounter > 20 :
            grudgecounter = 20
        total = stack.qsize()
        i = 0
        tempgrudge = 0
        while i < total :
            element = stack.get()
            if element == "confess\n" or element == "confess" :
                tempgrudge += 1
            i += 1
        f = open("storage.txt", "a")
        f.write(str(args.last_opponent_move) + "\n")
        f.close()
        f = open("grudge.txt", "w")
        f.write(str(grudgecounter))
        f.close()
        finalcalc = grudgecounter * (tempgrudge / total)
        decider = random.randint(0,19)
        if finalcalc > decider :
            print("confess")
        else :
            print("silent")

