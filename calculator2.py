#Pair programming by emilymlam & vianey81
from arithmetic import *

valid_entries = ["+","-","*","/","square","cube","pow","mod"]
print "This is a calculator. Enter a valid math operator to find the answer or enter 'q' to exit. Valid operators are:"
print ",".join(valid_entries)
print "For example, to add 2 and 2, input: + 2 2\n"

while True:
    tokens = raw_input("Enter a math function: ").split(" ")
    for i in range(1,len(tokens)):
        tokens[i] = int(tokens[i])

    if tokens[0] not in valid_entries:
        print "That's not a valid entry. Exiting."
        break
    else:
        if tokens[0]=="+":
            print add(tokens[1],tokens[2])
        if tokens[0]=="-":
            print subtract(tokens[1],tokens[2])
        if tokens[0]=="*":
            print multiply(tokens[1],tokens[2]) 
        if tokens[0]=="/":
            print divide(tokens[1],tokens[2])
        if tokens[0]=="square":
            print square(tokens[1]) 
        if tokens[0]=="cube":
            print cube(tokens[1])
        if tokens[0]=="pow":
            print power(tokens[1],tokens[2])
        if tokens[0]=="mod":
            print mod(tokens[1],tokens[2])
