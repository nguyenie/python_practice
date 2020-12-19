def animals():
    print("How many chickens are there? ") # print statement
    chickens = float(input())
    if chickens < 0: # if the users number of chickens is negative print:
        print("⚠Your number of hours must be GREATER than 0⚠")



    print("How many cows are there? ")
    cows = float(input())
    if cows < 0:# if the users number of cows is negative print:
        print("⚠Your number of hours must be GREATER than 0⚠")

    print("How many pigs are there? ")
    pigs = float(input())
    if pigs < 0:# if the users number of pigs is negative print:
        print("⚠Your number of hours must be GREATER than 0⚠")

    if pigs and cows and chickens < 0: # if the users number of chickens, cows, or pigs is negative print:
        print("Error: Could not solve ")

    if pigs and cows and chickens > 0: # if the users number of chickens is greater than 0 continue
        total = (chickens * 2) + (cows * 4) + (pigs * 4)
        print("animals (", chickens, ",", "cows", ",", "pigs", ",", ")", "➞", total)
animals()


