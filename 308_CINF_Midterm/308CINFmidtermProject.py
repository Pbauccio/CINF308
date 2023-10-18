# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:53:12 2023

@author: pbauc
"""
#Global Lists
Customer_List = []
Log_List = []

#function for gathering user info
def Add_Customer(Customer_List, Log_List):
    Name = input("Enter your name here: ")
    
    #Input for birthday information
    Birth_Year = input("Enter your birth year here: ")
    Birth_Month = input("Enter your birth month here: ")
    Birth_Day = input("Enter your birth day here: ")
    
    #Input for location information
    City = input("Enter the city you're in here: ")
    State = input("Enter the state you're in here: ")
    
    #Organize the input inforamtion given 
    #Convert them to strings so they could later be added to a text file
    Birthday_Tuple = (Birth_Month, Birth_Day, Birth_Year)
    Birthday_String = str(Birthday_Tuple)
    
    Location_Tuple = (City, State)
    Location_String = str(Location_Tuple)
        
    #Info stored into the a list called User info 
    User_Info = (Name, Birthday_String, Location_String)
    User_Info_String = str(User_Info)
    
    #Add user info to new list 
    Customer_List.append(User_Info_String)
    
    #Add action to log system
    Log_List.append(" Customer Added,")
    
    
#Remove Customer function
def Remove_Customer(Customer_List, Log_List):
    print("Here is the list of current customers: ")
    print(Customer_List)
    Which_Customer = int(input("\nEnter the number customer you would like to remove. (The first customer is customer number 0): "))
    
    # Remove the element at the specified index
    if 0 <= Which_Customer < len(Customer_List):
        Removed_Customer = Customer_List.pop(Which_Customer)
        print(f"\nThe customer at index {Which_Customer} ({Removed_Customer}) has been removed.")
    else:
        print("Invalid selection. Please enter a valid selection.")
    print("\nHere is the new list of customers:", Customer_List)
    
    #Add action to log system
    Log_List.append(" Customer Removed,")
    
#View customer details function
def Customer_Details(Customer_List):
    print("Here is the list of current customers: ")
    print(Customer_List)
    Customer_Log = ', '. join(Customer_List)
    Log_List.append(" Checked Customer Details,")
    Customer_Choice = input("Would you like this exported to a text file? Type in Y or N: ")
    if Customer_Choice == "Y" or Customer_Choice == "y":
        file = open("CustomerList.txt", "w")
        file.writelines(Customer_Log)
        file.close()
        print("Understood")
    elif Customer_Choice == "N" or Customer_Choice == "n":
        print("Customer log was not exported.")
    else:
        print("Invalid option. Please try again.")
    
#Log list function
def Log_System(Log_List):
    print("Here is the log of interactions: ")
    print(Log_List)
    Log_List.append(" Checked Log System,")
    Customer_Choice = input("Would you like this exported to a text file? Type in Y or N: ")
    if Customer_Choice == "Y" or Customer_Choice == "y":
        file = open("LogRecords.txt", "w")
        file.writelines(Log_List)
        file.close()
        print("Understood")
    elif Customer_Choice == "N" or Customer_Choice == "n":
        print("log Records were not exported.")
    else:
        print("Invalid option. Please try again.")

Option = "1" 
while Option != "5":
    print("\nHello welcome to the CRM!\nHere are the available options")
    print("\nOptions:")
    print("1. Add New Customer")
    print("2. Remove Customer")
    print("3. View Customer Details")
    print("4. Interactions Log")
    print("5. Quit")
    Option = input("Enter your choice here: ")
    
    
    #When an option is selected it will go through these series of statments
    if Option == "1":
        Add_Customer(Customer_List, Log_List)
    elif Option == "2":
        Remove_Customer(Customer_List, Log_List)
    elif Option == "3":
        Customer_Details(Customer_List)
    elif Option == "4":
        Log_System(Log_List)
    elif Option == "5":
        break #This acts as a quit function
    else:
        print("Invalid option. Please try again.")