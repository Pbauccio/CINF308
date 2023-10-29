# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:21:10 2023

@author: pbauc
"""
#Function for stating whether game is found on the list and where it is located 
def Search_Game(List, Game):
    if Game in List:
        return f"{Game} found at index {List.index(Game)}."
    else:
        return f"{Game} not found in the list."

#Function confirming game was inserted at the desired spot on the list
def Insert_Game(List, Index, Game):
    List.insert(Index, Game)
    return f"{Game} inserted at index {Index}."

#List for favorite Nintendo Switch games
Games_List = ["Mario Odyssey", "Pikmin 4", "Mario Wonder", "Super Mario 3D All-Stars", "Breath of The Wild"]

#Menu for user to see. In addition it shows a series of options for the user
while True:
    print("\nWelcome to your top games list!")
    print("\nCurrent list of games:", Games_List)
    print("\nSelect your option!:")
    print("1. Search")
    print("2. Insert")
    print("3. Quit")

    Choice = input("Enter your choice (1/2/3): ")

#Series of if and elif statements for when the user picks an option 1-3 and if they pick an invalid one
    if Choice == '1':
        Search_Game_Value = input("Enter the game to search: ")
        Result = Search_Game(Games_List, Search_Game_Value)
        print(Result)
    elif Choice == '2':
        Insert_Index = int(input("Enter the index(spot) to insert: "))
        Insert_Value = input("Enter the game you would like to add: ")
        Result = Insert_Game(Games_List, Insert_Index, Insert_Value)
        print(Result)
    elif Choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

print("Nice list!")
