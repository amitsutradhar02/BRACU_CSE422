# -*- coding: utf-8 -*-
"""22201054_Amit Sutradhar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iUiIwhw-lDEUbs9-tv2uoT-JDuThxRap
"""

# Problem 01

import random
import math

def strength(x):

    return math.log2(x + 1) + (x / 10)

def utility(maxV,minV):
    i = random.choice([0, 1])
    rand_component = (-1) ** i * random.randint(1,10) / 10
    return strength(maxV) - strength(minV) + rand_component

def minimax(depth,is_max,alpha,beta,maxV,minV):
    if depth == 0:
        return utility(maxV,minV)

    if is_max:
        max_eval = float('-inf')
        for i in range(2):  #Two possible moves
            eval = minimax(depth - 1,False,alpha,beta,maxV,minV)
            max_eval = max(max_eval,eval)
            alpha = max(alpha,eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for j in range(2):
            eval = minimax(depth - 1,True,alpha,beta,maxV,minV)
            min_eval = min(min_eval,eval)
            beta = min(beta,eval)
            if beta <= alpha:
                break
        return min_eval

def play_game(starting_player,maxV,minV):

    if starting_player == 0:  #Carlsen is Max
        result = minimax(5,True,float('-inf'),float('inf'),maxV,minV)
    else:  #Caruana is Max
        result = minimax(5,True,float('-inf'),float('inf'),minV,maxV)

    if result > 0:
        return "Magnus Carlsen", result
    elif result < 0:
        return "Fabiano Caruana", result
    else:
        return "Draw", result

def main():
    starting_player = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
    carlsen_strength = float(input("Enter base strength for Carlsen: "))
    caruana_strength = float(input("Enter base strength for Caruana: "))

    carlsen_wins = 0
    caruana_wins = 0
    draws = 0

    for k in range(4):
        winner, utility_value = play_game(starting_player, carlsen_strength, caruana_strength)
        print(f"Game {k + 1} Winner: {winner} (Utility value: {utility_value:.2f})")

        if winner == "Magnus Carlsen":
            carlsen_wins += 1
        elif winner == "Fabiano Caruana":
            caruana_wins += 1
        else:
            draws += 1

        #Switch starting player for the next game
        starting_player = 1 - starting_player

    print("\nOverall Results:")
    print(f"Magnus Carlsen Wins: {carlsen_wins}")
    print(f"Fabiano Caruana Wins: {caruana_wins}")
    print(f"Draws: {draws}")

    if carlsen_wins > caruana_wins:
        print("Overall Winner: Magnus Carlsen")
    elif caruana_wins > carlsen_wins:
        print("Overall Winner: Fabiano Caruana")
    else:
        print("Overall Winner: Draw")


main()

# Problem 02

def chess_noobs():
    first_player = int(input("Enter who goes first (0 for Light, 1 for L): "))
    mind_control_cost = float(input("Enter the cost of using Mind Control: "))
    light_strength = float(input("Enter base strength for Light: "))
    l_strength = float(input("Enter base strength for L: "))


    minimax_value_without_mc = minimax(5, first_player == 0,float('-inf'),float('inf'),light_strength,l_strength)

    if first_player == 0:
        minimax_value_with_mc = minimax(5,False,float('-inf'),float('inf'),light_strength,l_strength)
        minimax_value_with_mc_after_cost = minimax_value_with_mc - mind_control_cost

    else:
        minimax_value_with_mc = minimax(5,True,float('-inf'),float('inf'),l_strength,light_strength)
        minimax_value_with_mc_after_cost = minimax_value_with_mc - mind_control_cost


    print(f"Minimax value without Mind Control: {minimax_value_without_mc:.2f}")
    print(f"Minimax value with Mind Control: {minimax_value_with_mc:.2f}")
    print(f"Minimax value with Mind Control after incurring the cost: {minimax_value_with_mc_after_cost:.2f}")

    #Decision making
    if first_player == 0:  #Light's turn
        if minimax_value_without_mc > 0:
            print("Light should NOT use Mind Control as the position is already winning.")

        elif minimax_value_with_mc_after_cost > 0:
            print("Light should use Mind Control.")

        else:
            print("Light should NOT use Mind Control as the position is losing either way.")

            if minimax_value_with_mc_after_cost < 0:
                print("Light should NOT use Mind Control as it backfires.")

    else:  #L's turn
        if minimax_value_without_mc < 0:
            print("L should NOT use Mind Control as the position is already winning.")

        elif minimax_value_with_mc_after_cost < 0:
            print("L should use Mind Control.")

        else:
            print("L should NOT use Mind Control as the position is losing either way.")

            if minimax_value_with_mc_after_cost < 0:
                print("L should NOT use Mind Control as it backfires.")

chess_noobs()