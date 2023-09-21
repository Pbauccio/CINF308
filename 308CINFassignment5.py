# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:53:12 2023

@author: pbauc
"""

#function for gathering user info
def Get_User_Info():
    Username = input("Enter your username here: ")
    
    #Input for birthday information
    Birth_Year = input("Enter your birth year here: ")
    Birth_Month = input("Enter your birth month here: ")
    Birth_Day = input("Enter your birth day here: ")
    
    #Input for location information
    City = input("Enter the city you're in here: ")
    State = input("Enter the state you're in here: ")
    
    
    #Organize the input inforamtion given 
    Birthday_Tuple = (Birth_Month, Birth_Day, Birth_Year)
    Location_Tuple = (City, State)
    
    #Dictionary to organize the info provided including the tuples
    User_Dictionary = {
        "Username": Username,
        "Birthday": Birthday_Tuple,
        "Location": Location_Tuple
        }
    
    #Info stored into the a list called User info 
    User_Info = [User_Dictionary["Username"], User_Dictionary["Birthday"], User_Dictionary["Location"] ]
    
    #Print and format the information inputted
    #Use join to format the strings in an organized manner
    print("\nUsername is: ", User_Dictionary["Username"])
    print("Birthday of this user is:"," " .join(User_Dictionary["Birthday"]))
    print("Location of this user is:",", " .join(User_Dictionary["Location"]))
    
Get_User_Info()
