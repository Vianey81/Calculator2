from arithmetic import *

print "Please enter a math function: "
valid_entries = ["+","-","*","/","square","cube","pow","mod"]

while True:
    tokens = raw_input().split(" ")
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
