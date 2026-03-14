#if and if-else statements 
name = input("Enter your name :")
age = int(input("Enter your age :"))
if age >= 18:
    print(name," you are Eligible for vote ")
else :
    print(name," you are NOT Eligible for vote ")
print("----------------------------------------------------------------------------------------")
#if-elif-else used when there are multiple conditions  
marks = int(input("Enter your marks :"))
if marks >= 90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >=50:
    print("Grade C")
else :
    print("Fail")    
print("----------------------------------------------------------------------------------------")
#logical conditon with and
age =int (input("Enter your age ;"))
has_id = input("Do you have Id (yes/no):")
if age >= 18 and has_id=="yes":
    print("Entry allowed! ")
else :
    print("Entry denied!")
print("----------------------------------------------------------------------------------------")
#nested if
num = int(input("Enter a number :"))
if num>= 0:
    if num ==0:
        print("The number is zero")
    else :
        print("the number is greater than zero")
else :
    print("The number is nagetive")

print("----------------------------------------------------------------------------------------")
#task 1 : take a number from user and tell that no is even or add
no = int(input("Enter a number :"))
if no%2 == 0:
    print("The number is even ")
else :
    print("the number is odd")
print("----------------------------------------------------------------------------------------")
#task 2 : print the greatest number from 3 numbers 
n1 = int(input("Enter 1st number :"))
n2 = int(input("Enter 2nd number :"))
n3 = int(input("Enter 3rd number :"))
if n1 > n2 and n1 > n3:
    print(n1,"is the greater number")
elif n2 > n1 and n2 > n3:
    print(n2,"is greater")
else :
    print(n3,"is greater")
print("----------------------------------------------------------------------------------------")
#task 3 : take username and passward and print login successful if both are correct
user = input("Enter your Username :")
pswd = input("Enter your password :")
if user == "admin" and pswd == "1234":
    print("Login Succeessfully !!")
else :
    print("Invalid Crediantials!")