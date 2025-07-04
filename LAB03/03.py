# -*- coding: utf-8 -*-
"""22301205_3_Assignment3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mOtavD3kc6sOASGZ4V7uUnnkwU2h5-zH
"""

#@title Part 1

import math

def alpha_beta_pruning(depth, idx, max_player, values, alpha, beta, max_depth = 5):
    if depth == max_depth:
        if 0 <= idx < len(values):
            return values[idx]
        else:
            return 0

    if max_player:
        best = -math.inf
        for i in range(2):
            var = alpha_beta_pruning(depth + 1, idx * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, var)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best

    else:
        best = math.inf
        for i in range(2):
            var = alpha_beta_pruning(depth + 1, idx * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, var)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

def mortal_kombat(player1):
    values = [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
    rounds = 0
    round_winners = []
    scorpion_wins = 0
    sub_zero_wins = 0

    result = alpha_beta_pruning(0, 0, player1 == 0, values, -math.inf, math.inf)

    if result == -1:
        overall_winner = "Sub-Zero"
    else:
        overall_winner = "Scorpion"

    while scorpion_wins < 2 and sub_zero_wins < 2:
        rounds += 1

        if rounds == 1:
            if overall_winner == "Sub-Zero":
                round_winner = "Scorpion"
            else:
                round_winner = "Sub-Zero"

        elif rounds == 2:
            round_winner = overall_winner

        else:
            round_winner = overall_winner

        round_winners.append(round_winner)

        if round_winner == "Scorpion":
            scorpion_wins += 1
        else:
            sub_zero_wins += 1

        player1 = 1 - player1

    print(f"Game Winner: {overall_winner}")
    print(f"Total Rounds Played: {rounds}")
    for i, winner in enumerate(round_winners, 1):
        print(f"Winner of Round {i}: {winner}")

player1 = int(input())
mortal_kombat(player1)

#@title Part 2

def pacman_game(c):

    values = [3, 6, 2, 3, 7, 1, 2, 0]

    def minimax(depth, idx, max_player):

        if depth == 3:
            return values[idx]

        if max_player:
            return max(minimax(depth + 1, idx * 2, False),
                       minimax(depth + 1, idx * 2 + 1, False))
        else:
            return min(minimax(depth + 1, idx * 2, True),
                       minimax(depth + 1, idx * 2 + 1, True))

    var = minimax(0, 0, True)
    left_value = max(values[0], values[1], values[2], values[3]) - c
    right_value = max(values[4], values[5], values[6], values[7]) - c

    if max(left_value, right_value) > var:
        if left_value > right_value:
            return f"The new minimax value is {left_value}. Pacman goes left and uses dark magic"
        else:
            return f"The new minimax value is {right_value}. Pacman goes right and uses dark magic"
    else:
        return f"The minimax value is {var}. Pacman does not use dark magic"

c = int(input("Enter the value of c: "))
result = pacman_game(c)
print(result)

#@title Part 2

values = [3, 6, 2, 3, 7, 1, 2, 0]

while True:
    c = int(input("Enter the value of c: "))
    break

result = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf, 3)
print(f"\nThe final value of the root node without using dark magic: {result}")

left_value = max(values[0], values[1], values[2], values[3]) - c
right_value = max(values[4], values[5], values[6], values[7]) - c

print(f"\nFinal root node value while using dark magic and going left: {left_value}")
print(f"Final root node value while using dark magic and going right: {right_value}")

if max(left_value, right_value) > result:
    print("\nUsing dark magic is advantageous for Pac-Man.")
    if right_value > left_value:
        print(f"It's more beneficial when Pac-Man goes right, with a value of {right_value}.")
    else:
        print(f"It's more beneficial when Pac-Man goes left, with a value of {left_value}.")
else:
    print("\nUsing dark magic is not advantageous for Pac-Man.")