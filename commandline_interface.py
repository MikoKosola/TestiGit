# ROCK PAPER SCISSORS CLI
import random
from game_logic import pick_winner

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