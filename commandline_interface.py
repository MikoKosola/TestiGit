# ROCK PAPER SCISSORS CLI
import random
from game_logic import pick_winner

print("Tervetuloa kivi-paperi-sakset peliin!")
print("Valitse pelimuoto:")
multiplayer = input("Are you playing against the computer? (y/n): ").lower()
if multiplayer == "y":
    print("You are playing against the computer.")

    while True:
        player_pick = input("Pick rock, paper or scissors: ").lower()
        if player_pick in ["rock", "paper", "scissors"]:
            break
    print(player_pick)
    cpu_pick = random.choice(["rock", "paper", "scissors"])
    print(cpu_pick)

    winner = pick_winner(player_pick, cpu_pick)
    if winner == "player":
        print("Voitit!")
    elif winner == "cpu":
        print("Hävisit!")
    else:
        print("Tasapeli!")

else:
    while True:   
        player_1_pick = input("Pick rock, paper or scissors: ").lower()
        if player_1_pick in ["rock", "paper", "scissors"]:
            break
    print(player_1_pick)

    while True:
        player_2_pick = input("Pick rock, paper or scissors: ").lower()
        if player_2_pick in ["rock", "paper", "scissors"]:
            break
    print(player_2_pick)

    winner = pick_winner(player_1_pick, player_2_pick)
    if winner == "player":
        print("Pelaaja 1 voitti!")
    elif winner == "cpu":
        print("Pelaaja 2 voitti!")
    else:
        print("Tasapeli!")