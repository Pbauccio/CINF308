# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 10:35:44 2023

@author: pbauc
"""
#This program will let you know your speed on the 100m dash
#Once it analyzes your time the program will see where your 100m time ranks in terms of skill

#Here will be a new class called SprintTechnique
#This chunk of code is used to represent compostion as "Runner" is composed of a "SprintTechnique" object
class SprintTechnique:
    def __init__(self, Evaluation):
        self.Evaluation = Evaluation
    
    def EvaluateTechnique(self):
        if self.Evaluation == "Great":
            return "\nYour sprinting technique is excellent!"
        elif self.Evaluation == "Average":
            return "\nYour sprinting technique is decent!"
        elif self.Evaluation == "Ok":
            return "\nYou need to work on your sprinting technique. Keep trying you can do it!"
        else:
            return "\nInvalid technique evaluation."

#Class for the runner/user
class Runner:
    def __init__(self, Distance, Gender, Time, SprintTechnique):
        self.Distance = Distance
        self.Gender = Gender
        self.Time = Time
        self.Sprint_Technique = SprintTechnique

        
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
        if (self.Gender == "F" or self.Gender == "f"):
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
    SprintTechniqueEval = input("How would you evaluate your sprinting technique (Great/Average/Ok): ")

    
    #Add values to the runner/user
    self = Runner(Distance, Gender, Time, SprintTechnique)
    
    #Add values to the SprintTechnique class
    Sprint_Technique = SprintTechnique(SprintTechniqueEval)

    #Formula for calculating the speed
    Speed = Runner.Calculate_Speed(self)
    
    #This will format speed so it goes to the second decimal place
    Speed = float(format(Speed, ".2f"))
    
    #States speed runner was going
    print("You were going", Speed, "meters per second \n")
    
    #States the runner's skill level
    Level = Runner.Determine_Level(self)
    print(f"You run at a {Level}!")
    
    #States level of technique runner has
    TechniqueEvaluation = Sprint_Technique.EvaluateTechnique()
    print(TechniqueEvaluation)
    
    #This while loop allows the user to restart the program if they choose so
    Restart = input("Would you like to run the program again Y/N? ")
    while Restart != "n" and Restart != "N" and (Restart != "y" and Restart != "Y"):
        restart = input("Would you like to run the program again Y/N? ")
print("Goodbye!")


    






