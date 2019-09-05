#Design an algorithm that finds the maximum positive integer input by a user.  
#The user repeatedly inputs numbers until a negative value is entered.
 
#Make sure that you write up the algorithm before starting to code.
#Then implement the algorithm in Python. Put your algorithmic description as a comment in the program file.

#During the design of your algorithm and your implementation, you should use git:
#Initialize a local directory with git init.
#Write the text of your algorithm in a file called max_int.py
#Inspect the result of git status
#Use git add . to move changes to the staging area.
#Commit your changes with git commit -m “Algorithm written for max_int”
#Then start implementing your algorithm
#During your implementation, make sure you do git status, git add, and git commit regularly.
#You can see a log of all your commits with git log.
#When you have finished your implementation:
#Create an account on github.com (if you don't already have it).
#Create a public repository on github
#Follow the instructions (that appear on github when you have created a new repository) under "push an existing repository from the command line"  (see also here)
#Push your changes to the remote repo with: git push
#Inspect your commits on github

# 1- Assign max_int to zero 
# 2- get a number from a user while the number is bigger than 0 and the number is not a negative number go through the while loop
# 3- if the input number is bigger than the max number wich is zero in the beginning
# 4- assign the input number (num_int) to max_int so that max_int = num_int
# 5- print the biggest number 
# 6- input a new number and go througt it again untill the number is an negative number


num_int = int(input("Input a number: ")) # Do not change this line
max_int = 0

while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    
    num_int = int(input("Input a number: ")) # Do not change this line 

