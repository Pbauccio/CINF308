# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:23:09 2023

@author: pbauc
"""
#Import matplotlib
import matplotlib.pyplot as plt

#These functions will be the chart visuals 
def Cost_Chart(Products, Item_Cost, Title):
    plt.figure(figsize=(10, 5))
    plt.bar(Products, Item_Cost, color='green')
    plt.xlabel('Products')
    plt.ylabel('Cost per item')
    plt.title(Title)
    plt.show()
    
def Supply_Chart(Products, Supply, TitleTwo):
    plt.figure(figsize=(10, 5))
    plt.bar(Products, Supply, color='blue')
    plt.xlabel('Products')
    plt.ylabel('Supply')
    plt.title(TitleTwo)
    plt.show()
    

#Loop that runs the script and asks for user input at the end
Restart = "y"
while Restart == "y" or Restart == "Y":
    #Lists and titles for charts
    Products = []
    Item_Cost = []
    Supply =[]
    Title = "Current Value Per Item"
    TitleTwo = "Supply Per Item"
        
    #Gets the amount of items are being analyzed along with the names of those products
    Number_Products = int(input("How many products would you like to analyze? "))
    while Number_Products > 0: 
        User_Product = input("Enter your product: ")
        Number_Products -= 1
        Products.append(User_Product)
        
    #Gets the cost of each product
    for x in Products:
        Product_Price = float(input(f"How does {x} cost? "))
        Item_Cost.append(Product_Price)
    
    #Gets the supply of each product 
    for x in Products: 
        Product_Supply = int(input(f"How many {x}'s are in supply? "))
        Supply.append(Product_Supply)
    
    #Runs each chart function
    Cost_Chart(Products, Item_Cost, Title)
    Supply_Chart(Products, Supply, TitleTwo)
    
    #Gets the potential value for each product and states it for the user
    for x in Products: 
        Index = Products.index(x)
        Product_Value = Item_Cost[Index] * Supply[Index]
        print(f"{x} has a total value of:", Product_Value, "dollars")
        
    #This while loop allows the user to restart the program if they choose so
    Restart = input("Would you like to run the program again Y/N? ")
    while Restart != "n" and Restart != "N" and (Restart != "y" and Restart != "Y"):
        restart = input("Would you like to run the program again Y/N? ")
print("Goodbye!")
    
