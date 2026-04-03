#basic function
def greet():
    print("Hello Sarika!!")
greet()
print("------------------------------------------------------------------------------------")

#function with single parameter
def greet(name):
    print("how are you",name,"?")
greet("Sarika")
print("------------------------------------------------------------------------------------")

#function with return value
def add(a,b):
    return a + b
result = add(5,3)
print("Addition :",result)
print("------------------------------------------------------------------------------------")

#task 1 : function to check no. is even or odd
def check_even(num):
    if num % 2 == 0 :
        print(num,"number is even")
    else :
        print(num,"number is odd")
num = int(input("Enter a number to check even or odd :"))
check_even(num)
print("--------------------------------------------------------------------------------------")

#task 2 : function to find maximum number 
def max_number(a,b,c):
    if a>b and a>c:
        print(a,"is the maximum number ")
    elif b>a and b>c:
        print(b,"is the maximum number")
    else :
        print(c,"is the maximum number")
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("enter 3rd number :"))
max_number(a,b,c)
print("-------------------------------------------------------------------------------------")

#task 3 : factorial of the number 
def factorial(n):
    if n == 0 or n== 1:
        return 1
    result = 1
    for i in range(1,n+1):
        result *= i
    print("Factorial of the number is :",result)
n = int(input("Enter a number to find factorial :"))
factorial(n)


