import argparse
import random
import json
from os.path import exists

############################################################################

# Name: Zachary Pownell
# Professor: Cary Jardin
# Class: CS311 Data Structures & Algorithms
# Date: 26 October, 2021

############################################################################

# Name of the opponent move history file.
OPPONENT_HISTORY_FILE = "opponent_history_file.json"
PARAM_FILE = "param_file.json"

# Params dictionary containing all my parameters.
params = {
    # If HOLD_A_GRUDGE = True, my agent will hold a grudge and confess for the duration of HOLD_A_GRUDGE_LENGTH.
    "hold_a_grudge": True,
    # How many turns my agent will hold a grudge (chooses confess) if the opponent chooses confess.
    "hold_a_grudge_length": 2,
    # Counter for holding a grudge. Ignore.
    "hold_a_grudge_counter": 0,
    # If RANDOM_CONFESS = True, randomly become confess if my agent chooses to silent.
    "random_confess": True,
    # Chooses a number between 1 - RANDOM_CONFESS_ODDS if RANDOM_CONFESS = True.
    "random_confess_odds": 100,
    # If BECOME_AGGRESSIVE = True, decrement RANDOM_CONFESS_ODDS by AGGRESSIVE_DECREMENT
    # until AGGRESSIVE_CAP is reached.
    "become_aggressive": True,
    "aggressive_decrement": 1,
    "aggressive_cap": 5
}

opponent_history = {
    "history": ""
}


# Dumps param or opponent history from program into json file.
def dump_file(file):

    if file == PARAM_FILE:
        with open(PARAM_FILE, "w") as f:
            json.dump(params, f)
    elif file == OPPONENT_HISTORY_FILE:
        with open(OPPONENT_HISTORY_FILE, "w") as f:
            json.dump(opponent_history, f)


# Loads param or opponent history from json file into program.
def load_file(file):

    if not exists(file):
        dump_file(file)
    with open(file) as f:
        return json.load(f)


# Print all the elements from arrays. For debugging purposes.
def print_data():

    print("\n\n\n-------------- PARAM FILE --------------")
    print(params)

    print("\n-------------- OPPONENT HISTORY FILE --------------")
    print(opponent_history)
    print("\n\n\n")


# Argparse initiation.
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')
    args = parser.parse_args()

    # Load up our param file and opponent history file.
    params = load_file(PARAM_FILE)
    opponent_history = load_file(OPPONENT_HISTORY_FILE)

    # Assign opponents_last_move to the opponents last move.
    opponents_last_move = args.last_opponent_move

    # Record our opponent history.
    try:
        opponent_history["history"] += opponents_last_move[0]
    except TypeError:
        pass
    # Save our opponent history to json file.
    dump_file(OPPONENT_HISTORY_FILE)

    # Opponent confessed.
    if opponents_last_move == "confess":

        # Check if hold a grudge is true.
        if params["hold_a_grudge"]:

            params["hold_a_grudge_counter"] = params["hold_a_grudge_length"]
            print("confess")

        # If hold a grudge is false, keep silent. Even if opponent's last move was confess.
        else:
            print("silent")

        # Now lets check if my agent will become more aggressive now that my opponent chose confess.
        if params["become_aggressive"]:

            if params["random_confess_odds"] >= params["aggressive_cap"]:

                params["random_confess_odds"] -= params["aggressive_decrement"]

    # Opponent silent.
    else:

        # If the hold_a_grudge_counter does not equal 0, confess and decrement hold_a_grudge_counter by 1.
        if params["hold_a_grudge_counter"] != 0:

            print("confess")
            params["hold_a_grudge_counter"] -= 1

        else:

            if params["random_confess"]:

                try:

                    if random.randint(0, params["random_confess_odds"]) == 0:

                        print("confess")

                    else:

                        print("silent")

                except ValueError:

                    print("silent")

            else:

                print("silent")

    # print_data()
    dump_file(PARAM_FILE)
    dump_file(OPPONENT_HISTORY_FILE)

