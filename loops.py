#printing numbers fron 1 to 10 using for loop
print("printing numbers from 1 to 10:")
for i in range(1,11):
    print(i)

print("-----------------------------------------------------------------")

#printing even numbers 
print("Even numbers from 1 to 20:")
for i in range(1,21):
    if i % 2==0:
        print(i)

print("-----------------------------------------------------------------")

#sum of 1 to n
n= int(input("Enter number to display sum from 1 to :"))
total = 0
for i in range(1,n+1):
    total += i
print ("Sum of numbers from 1 to",n,"is :",total)

print("-----------------------------------------------------------------")

#printing 1 to 10 using while loop
i = 1
while i<=10:
    print(i)
    i+= 1

print("-----------------------------------------------------------------")

#reverse counting 
i= 10 
while i >= 1:
    print(i)
    i -=1

print("-----------------------------------------------------------------")

#factorial of the number 
num = int(input("Enter a number to find factorial :"))
fact =1
for i in range(1,num+1):
    fact *= i
print("Factorial of the number is :",fact)

print("-----------------------------------------------------------------")

#multiplication table 
numm = int(input("Enter a number to display table :"))
for i in range(1,11):
    print(numm,"x",i,"=",numm*i)

print("-----------------------------------------------------------------")

#count digits in a number 
n = int(input("Enter a number for finding digits :"))
count = 0
while n > 0:
    count += 1
    n //= 10
print("Digits :",count)

print("-----------------------------------------------------------------")

#reverse a number 
n= int(input("Enter a number to print reverse :"))
rev = 0
while n>0:
    digit = n%10
    rev = rev * 10 + digit
    n //= 10
print("Reverse of the number :",rev)

print("-----------------------------------------------------------------")

#print the pattern 1
for i in range(1,6): #for rows
    for j in range(i): #for stars 
        print("*",end="")
    print()

#print the pattern 2
for i in range(1,6): #for rows
    for j in range(i-1): #for stars 
        print("*",end="")
    print()