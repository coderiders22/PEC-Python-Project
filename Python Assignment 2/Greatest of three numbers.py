#-------------------------------------------------------------------------------
# Name:        Manav Rai
# Branch:     Computer Science Engineering (Data Science)
# Purpose:    Write a python program to find the greatest of three numbers
#             entered by the user.
#
# Question No. : 4
#
# Created:     11-12-2022
#-------------------------------------------------------------------------------

#To find greatest of three numbers

#Try to use input to evaulate the greatest of the numbers
try:
    #Get input from user
    a = eval(input("Enter number 1: "))
    b = eval(input("Enter number 2: "))
    c = eval(input("Enter number 3: "))

    #Compare inputs
    if a > b and a > c:
        print(a, "is the greatest")
    if b > a and b > c:
        print(b, "is the greatest")
    if c > a and c > b:
        print(c, "is the greatest")
    print("yes.")


except:
    print ("Enter a valid number!")
    print("no.")