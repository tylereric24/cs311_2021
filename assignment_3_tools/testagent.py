import argparse
import random
import json


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()

    num_moves = 0
    past_moves = []
    #To make sure that the file exists
    with open("grievances.json", "a") as f: 
        pass
    #Reads past opponent moves into past_moves list
    with open("grievances.json", "r") as openfile: 
        try:
            past_moves = json.load(openfile)
            num_moves = (past_moves.pop())
        except:
            past_moves = []

    #Keeps track of what iteration we're in
    num_moves += 1
    #Loads last move argument into last_move
    last_move = args.last_opponent_move 

    #Appends current iteration's past move
    if last_move == 'silent' or last_move == 'confess':
        past_moves.insert(0, last_move)

    #Keeps total recorded moves under a value
    if len(past_moves) > 5:
    	past_moves.pop()

    ######################################################################### Work in here
    decision = 'silent' #random.choice(['confess', 'silent'])
    if num_moves > 1 and num_moves < 100:
        #Insert Decision making here
        num_silent = 0
        num_confess = 0
        for i in past_moves:
            if i == 'silent':
                num_silent += 1
            elif i == 'confess':
                num_confess += 1

	#This is where the magic happens
        if num_confess > num_silent:
            decision = 'confess'
        else:
            decision = 'silent'

    elif num_moves > 99:
        decision = 'confess'

    #########################################################################

    #Saves number of moves into the list to be saved into the json for use in next iteration
    if num_moves < 100:
        past_moves.append(num_moves)
    else:
        #If over iteraetion limit, wipes the past_moves, Functions to make sure nothing carries over if the grievances file is not deleted between tournament iterations
        past_moves = []

    #Creates json format to be written
    save_moves = json.dumps(past_moves) 

    #Saves the past moves list into a file for use in next iteration
    with open("grievances.json", "w") as outfile:
        outfile.write(save_moves)

    #Prints output decision
    print(decision) #decision being the string output, either 'confess' or 'silent' based on algorithm
    
