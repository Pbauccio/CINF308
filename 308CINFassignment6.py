# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:18:24 2023

@author: pbauc
"""
#Import random to add a luck element
import random 

#Dictionary to organize the user's profile and their stats
Gamer = {
"Username": "",
"Level": 1,
"Score": 0
        }

#Mario enemy tuple
Mario_Enemies = ("Goomba", "Koopa", "Piranha Plant")
Random_MarioEnemy = random.choice(Mario_Enemies)

#Kirby enemy tuple
Kirby_Enemies = ("Blade Knight", "Gordo", "Bomber")
Random_KirbyEnemy = random.choice(Kirby_Enemies)

#Link enemy tuple
Link_Enemies = ("Bokoblin", "Chuchu", "Guardian Stalker")
Random_LinkEnemy = random.choice(Link_Enemies)


#Stroyline with various Nintendo themed locations
Storylines = {
    "The Forgotten Land" : {
        "Good Ending" : "You defeat Chaos Elfilis!",
        "Bad Ending" : f"You get hit by a {Random_KirbyEnemy} and lose some health."
        },
    "Mushroom Kingdom" : {
      "Good Ending" : "You defeat Bowser!",
      "Bad Ending" : f"You get hit by a {Random_MarioEnemy} and lose some health."
      },
    "Hyrule" : {
      "Good Ending" : "You defeat Ganondorf and save Zelda!",
      "Bad Ending" : f"You get hit by a {Random_LinkEnemy} and lose some health."
      }
}

#Each storyline's difficulty
Difficulty = {
    "The Forgotten Land": 1,
    "Mushroom Kingdom" : 2,
    "Hyrule" : 3
    }

#Actions the player could take. Note we are using a list 
Actions = ["Explore", "Leave"]

#Here is where the game function will begin
def Game():
    print("Welcome to the Nintendo Adventure Game!!")
    Gamer["Username"] = input("What is your name?: ")
    
    #A storyline will be randomly selected 
    Chosen_Storyline = random.choice(list(Storylines.keys()))
    print(f"You find yourself in {Chosen_Storyline}. ")
    
    #Main Game loop 
    while True:
        print(f"\nOptions: {', '.join(Actions)}")
        Action = input("What will you do? ")
        
        if Action not in Actions:
            print("Invalid action! Please select again")
            continue
        
        if Action == "Leave":
            print(f"You leave {Chosen_Storyline} safely. ")
            break
        
        #Calculate the success of their action
        Success_Chance = random.uniform(0,4) + (Gamer["Level"]/10)
        if Success_Chance > Difficulty[Chosen_Storyline]:
            print(Storylines[Chosen_Storyline]["Good Ending"])
            Gamer["Score"] += 10
            Gamer["Level"] += 1
        else:
            print(Storylines[Chosen_Storyline]["Bad Ending"])
            Gamer["Level"] -=1
            
        print(f"\nYour current stats: Level {Gamer['Level']}, Score {Gamer['Score']}")
        
    print(f"\nThanks for playing, {Gamer['Username']}!")

#Enter function here 
Game()