#operators in python 
print("Arithmatic Operators :")
a=100
b=2
print("Addition of a and b :",a+b)
print("Subtraction of a and b :",a-b)
print("multiplication of a and b :",a*b)
print("division of a and b :",a/b)
print("modulus of a and b :",a%b)#gives remainder after division
print("exponential(power) of a and b :",a**b)#power 
print("------------------------------------------------------------------------")

print("Assignment operator :")
print("Assignment operator = is used to assign a value to a variable ex., x=5")
x=5 
print("value of x :",x)
print("------------------------------------------------------------------------")
 
print("Comparision Operators :")
x=30
y=10
print("x > y :",x > y)
print("x < y :",x < y)
print("x == y :",x == y)
print("x != y :",x != y)
print("x >= y :",x >= y)
print("x <= y :",x <= y)
print("------------------------------------------------------------------------")

print("Logical Operators :")
age= 20
has_id= True
print("Allowed to Enter :",age > 18 and has_id )
print("Special condition :", age > 18 and has_id)
print("Reverse condition :", not has_id)
print("------------------------------------------------------------------------")

print("identity Operator :")
p= ["apple","banana"]
q=["apple","banana"]
r=p
print(p is r)
print(p is q)
print(p == q)
print("------------------------------------------------------------------------")

print("membership Operator :")
fruits=["apple","banana","cherry"]
print("banana" in fruits)
print("pineapple" not in fruits)
print("------------------------------------------------------------------------")

print("bitwise Operator :")
print(6 & 3)#binary representation of 6 is 0110 and 3 is 0011 then & operator will compares the bits and returns 0010, whichh is 2 in decimal 
print(6 | 3)#binary representation of 6 is 0110 and 3 is 0011 then | operator will compares the bits and returns 0111, which is 7 in decimal
print(6 ^ 3)#binary representation of 6 is 0110 and 3 is 0011 then ^ operator will compares the bits and returns 0101, which is 5 in decimal

#task1 
print("------------------------------------------Task 1--------------------------------------------------------")
num1= int(input("Enter a number :"))
num2 = int(input("Enter another no. :"))
print("remainder of the division :",num1 % num2)
print("Multiplicaton of no.s :",num1 * num2)

#task 2
print("-----------------------------------------Task 2-------------------------------------------------------------")
age = int (input("Enter your Age :"))
if age > 18:
    print("Eligible for vote !")
else :
    print ("Not Eligible for vote !")