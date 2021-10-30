import os
import argparse
import random
import subprocess



def run_game(player_a, player_b):
    players = [player_a, player_b]
    iterations = 100 
    for i in range(2):
        p = players[i]
        p['game_years'] = 0 
        p['last_move'] = "zero"
        p['current_move'] = "zero"

    for i  in range(iterations):
        for i in range(2):
            p = players[i] 
            if i == 0:
                proc = subprocess.Popen([f"{p['runme']} --init true --iterations {iterations}"], 
                        stdout=subprocess.PIPE, shell=True , cwd= p['dir_name'])
                (out, err) = proc.communicate()
    
            last_move = players[0]['last_move'] if i == 1 else players[1]['last_move']
            proc = subprocess.Popen([f"{p['runme']} --last_opponent_move {last_move}"],
                    stdout=subprocess.PIPE, shell=True , cwd= p['dir_name'])
            (out, err) = proc.communicate()
            #print(out)
            p['current_move'] = out.strip().lower().decode("utf-8")


        #score it!
        if players[0]['current_move'] == "confess" and players[1]['current_move'] == "confess":
            players[0]['game_years'] = players[0]['game_years'] + 5 
            players[1]['game_years'] = players[1]['game_years'] + 5 
        elif players[0]['current_move'] == "confess" and players[1]['current_move'] == "silent":
            players[0]['game_years'] = players[0]['game_years'] + 0 
            players[1]['game_years'] = players[1]['game_years'] + 20
        elif players[0]['current_move'] == "silent" and players[1]['current_move'] == "confess":
            players[0]['game_years'] = players[0]['game_years'] + 20
            players[1]['game_years'] = players[1]['game_years'] + 0 
        elif players[0]['current_move'] == "silent" and players[1]['current_move'] == "silent":
            players[0]['game_years'] = players[0]['game_years'] + 1 
            players[1]['game_years'] = players[1]['game_years'] + 1 
        else:
            print(players)
            print("!!!!!!!!!!!!!!!!!!!!Error!!!!!!!!!!!!!!")
        players[0]['last_move'] = players[1]['current_move'] 
        players[1]['last_move'] = players[0]['current_move']

    if players[0]['game_years'] > players[1]['game_years']:
        print(f"Player {players[1]['player name']} wins {players[1]['game_years']} < {players[0]['game_years']}")
    elif players[1]['game_years'] > players[0]['game_years']:
        print(f"Player {players[0]['player name']} wins {players[0]['game_years']} < {players[1]['game_years']}")
    else:
        print(f"Tie {players[0]['game_years']} = {players[1]['game_years']}")


PULL_DIR = "repos"

fork_list = []
with open("forkme.list", "r") as f:
    all_forks = f.read()
    for ffork in all_forks.split('\n'):
        parts = ffork.split()
        # example line ['@atilla20cs', 'atilla20cs', '/', 'cs311_2021']
        if len(parts) != 4:
            continue
        fork_list.append( {"github_user" : parts[1], "repo" : parts[3]} )


#clean up
os.system(f"rm -rf {PULL_DIR}")

players = []
bad_players = []
#load them up
for f in fork_list:
    os.system(f"mkdir -p {PULL_DIR}/{f['github_user']}")
    exec_me = f"git clone git@github.com:{f['github_user']}/{f['repo']}.git {PULL_DIR}/{f['github_user']}"
    os.system(exec_me)

    try:
        with open(f"{PULL_DIR}/{f['github_user']}/assignment3/runme.txt", "r") as runtxt:
            players.append({"player" : f"{f['github_user']}", "runtxt" : runtxt.read()})
    except:
        bad_players.append(f['github_user'])
        print(f"!!!!!!!!!!! Player {f['github_user']} did not load!!!!!!")



print("Good")
for p in players:
    print(p)
for p in bad_players:
    print(p)


run_game(players[0], players[1])

#run_txt = ""
#with open("runme.txt", "r") as f:
#    run_txt = f.read().strip()

#os.system(f"{run_txt} --help")





