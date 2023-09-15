# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:21:02 2023

@author: pbauc
"""
#Global Variables
#List of available games
Available_Games = ["Smash Ultimate", "Pikmin 4", "Animal Crossing", "Mario Odyssey"]
#List of games in the user's shopping cart
Games_In_Cart = []

#Function that allows user to see what games are taken or not
def Games_Lists(Available_Games, Games_In_Cart):
    print("\nCurrently available games:\n")
    for Game in Available_Games: #Printing with a for statement allows the brackets to disappear when printing
        print(Game)
    print("\nGames in cart:\n")
    for Game in Games_In_Cart:
        print(Game)
    
#Function that allows user to move Game
def Move_Game(Available_Games, Games_In_Cart):
    Game = input("Enter the game you want to move: ")
    if Game in Available_Games:
        Available_Games.remove(Game) #remove removes the game
        Games_In_Cart.append(Game) #append adds the game 
        print("Game has been moved to your cart.")
    elif Game in Games_In_Cart:
        Games_In_Cart.remove(Game)
        Available_Games.append(Game)
        print("Game has been moved to currently available games.")
    else:
        print("This game is not in available or in your cart.")
    
        
#Here we use a "while loop" in order for it to continuously ask until instructed otherwise
Option = "1" 
while Option != "3":
    print("\nHello welcome to the Nintendo eShop!\nHere are our available games:")
    Games_Lists(Available_Games, Games_In_Cart)
    print("\nOptions:")
    print("1. Move Game")
    print("2. Start Over")
    print("3. Quit")
    Option = input("Enter your choice here: ")
    
    #When an option is selected it will go through these series of statments
    if Option == "1":
        Move_Game(Available_Games, Games_In_Cart)
    elif Option == "2":
        Available_Games = ["Smash Ultimate", "Pikmin 4", "Animal Crossing", "Mario Odyssey"]
        Games_In_Cart = []
    elif Option == "3":
        break #This acts as a quit function
    else:
        print("Invalid option. Please try again.")
    


