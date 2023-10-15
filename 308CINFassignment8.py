# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 10:35:44 2023

@author: pbauc
"""
#This program will let you know your speed on the 100m dash
#Once it analyzes your time the program will see where your 100m time ranks in terms of skill

#Class for the runner/user
class Runner:
    def __init__(self, Distance, Gender, Time):
        self.Distance = Distance
        self.Gender = Gender
        self.Time = Time
        
    #Formula for calculating the speed of 
    def Calculate_Speed(self):
        return self.Distance/self.Time
    
    #Used to determine skill level based on time and gender competing in 
    def Determine_Level(self):
        if (self.Gender == "M" or self.Gender == "m"):
            if 10.50 <= self.Time <= 10.95:
                return "Division 1 level"
            elif 10.96 <= self.Time <= 11.20:
                return "Division 2 level"
            elif 11.21 <= self.Time <= 11.50:
                return "Division 3 level"
            elif 11.51 <= self.Time:
                return "High School level"
            elif 10.49 >= self.Time:
                return "Pro level"
        if (self.Gender == "F" or self.Gender == "F"):
            if 11.90 <= self.Time <= 12.40:
                return "Division 1 level"
            elif 12.41 <= self.Time <= 12.90:
                return "Division 2 level"
            elif 12.91 <= self.Time <= 13.50:
                return "Division 3 level"
            elif 13.51 <= self.Time:
                return "High School level"
            elif 11.89 >= self.Time:
                return "Pro level"


#loop so the program will continous run until told not to
Restart = "y"
while Restart == "y" or Restart == "Y":
    
    #100 for the 100 meters
    Distance = 100
    
    #This will ask for the users time. Note this is in seconds since it is the 100m
    #It will also ask for the gender you are competing in. So the level results can  be more accurate
    #The levels are by division in the NCAA
    Gender = input("what gender do you compete in, Male or female, (M or F): ")
    Time = float(input("What time did you finish the 100m dash: "))
    
    #Add values to the runner/user
    self = Runner(Distance, Gender, Time)
    #Formula for calculating the speed
    Speed = Runner.Calculate_Speed(self)
    
    #This will format speed so it goes to the second decimal place
    Speed = float(format(Speed, ".2f"))
    
    #States speed runner was going
    print("You were going ", Speed, "meters per second \n")
    
    #States the runner's skill level
    Level = Runner.Determine_Level(self)
    print(f"You run at a {Level}!")
        
    #This while loop allows the user to restart the program if they choose so
    Restart = input("Would you like to run the program again Y/N? ")
    while Restart != "n" and Restart != "N" and (Restart != "y" and Restart != "Y"):
        restart = input("Would you like to run the program again Y/N? ")
print("Goodbye!")


    






