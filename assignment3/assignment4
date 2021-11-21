import argparse
import random
import json
from os.path import exists

opp_moves_history = "opp_moves_history.json"
parameter_storage = "parameter_storage.json"

parameters = {
   
    "anger": True,
    "grudgelength": 4,
    "spill_the_beans": True,
    "spill_the_beans_odds": 200,
    "be_petty": True,
    "nuclear": 0,
    "petty_counter": 1,
    "petty_cap": 3,
    "iterations": 0,
    "chip_counter": 0
}

opponent_history = {
    "history": ""
}



def save_file(file):

    if file == parameter_storage:
        with open(parameter_storage, "w") as f:
            json.dump(parameters, f)
    elif file == opp_moves_history:
        with open(opp_moves_history, "w") as f:
            json.dump(opponent_history, f)

def load_file(file):
  
    if not exists(file):
        save_file(file)
    with open(file) as f:
        return json.load(f)

def print_data():

    print("\nParameter File")
    print(parameters)
    print("\n-Opp History-")
    print(opponent_history)
    print("\n")

if __name__ == "__main__":

    
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')
    args = parser.parse_args()
   
    is_new_game = args.init
    iterations = args.iterations
    opponents_last_move = args.last_opponent_move
  
    if is_new_game is not None:
        save_file(parameter_storage)
        save_file(opp_moves_history)
    else:
       
        parameters = load_file(parameter_storage)
        opponent_history = load_file(opp_moves_history)
   
    try:
        opponent_history["history"] += opponents_last_move[0]
    except TypeError:
        pass

    
    save_file(opp_moves_history)

   
    if iterations is not None:
        parameters["iterations"] = int(iterations)

    
    parameters["iterations"] -= 1

    
    if opponents_last_move == "confess":
        parameters["nuclear"] += 1

       
        if parameters["nuclear"] > 10:

           
            parameters["chip_counter"] < parameters["grudgelength"]
            print("confess")

       
        else:
            print("silent")

       
        if parameters["be_petty"]:

            if parameters["spill_the_beans_odds"] >= parameters["petty_cap"]:

                parameters["spill_the_beans_odds"] -= parameters["petty_counter"]
   
    else:

        
        if parameters["iterations"] < 3:

                r  = random.randint(0,5)

                if r == 0:
                    print("confess")
                  
    
                if parameters["iterations"] > 97:
                    b = random.randint(1,10)
                    if b == 10:
                        print("confess")
           
        else:

           
            if parameters["chip_counter"] != 0:

               
                print("confess")
                parameters["chip_counter"] -= 1

           
            else:

                
                if parameters["spill_the_beans"]:

                   
                    try:
                        t = random.randint(0,10)
                      
                        if t == 0:
                            print("confess")
                                         
                        else:
                            print("silent")

                    
                    except ValueError:

                        print("silent")

                
                else:

                    print("silent")

   
    save_file(parameter_storage)
    save_file(opp_moves_history)
