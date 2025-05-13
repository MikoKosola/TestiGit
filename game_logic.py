def pick_winner(player_pick, cpu_pick):
    if player_pick == cpu_pick:
        return "draw"
    elif (player_pick == "rock" and cpu_pick == "scissors") or \
         (player_pick == "scissors" and cpu_pick == "paper") or \
         (player_pick == "paper" and cpu_pick == "rock"):
        return "player"
    else:
        return "cpu"
