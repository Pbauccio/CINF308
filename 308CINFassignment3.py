# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:33:22 2023

@author: pbauc
"""
#Paul Bauccio

#Global varaible for the output file
file = open ( 'text.txt' , 'w' )

#Ask the user for their password and writes it down in the file that the question has been asked
password = input("Hello there! Please type in your password ")

#Used a while loop to check if length of password is equal to or less than 7
#If so it will ask the user to type in a password again
#when it is greater than or equal to 8 the program will write the password in the text file
while len(password) <= 7:
    print("\nYour password should to be atleast eight characters long")
    password = input("Please type in your password ")
else:
    file.write(password)


#Closes file to complete the writing portion
file.close()

 
#Opens the file in read 
file = open ('text.txt' , 'r')

#This will print stating the password is secure
print("\nPassword",file.readline(), "is a secure password")

#This will check if the password contains any numbers
if (any(map(str.isdigit, password))) == False:
    print("\nnext time include numbers in your password")

#Closes file to complete the reading portion
file.close()