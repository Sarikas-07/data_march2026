#print the pattern 1
for i in range(1,6): #for rows
    for j in range(i): #for stars 
        print("*",end="")
    print()

print("----------------------------------------------------------------")

#print the pattern 2
for i in range(5,0,-1): #for rows and -1 for decreasing 
    for j in range(i): #for stars 
        print("*",end="")
    print()

print("----------------------------------------------------------------")
