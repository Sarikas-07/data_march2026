# task 1 - variables and data types 
#integer 
age = 21
print("Age :", age)
print("Type of age :",type(age))#type() will identify the type of object at runtime

#float
cgpa= 7.7
print("CGPA :",cgpa)
print("Type of CGPA :",type(cgpa))

#string 
name="Sarika"
print("Name :",name)
print("Type of name :",type(name))

#boolean
is_student= True
print("is student :",is_student)
print("Type of is_student ;",type(is_student))

#-------------------------------------------------------------------------------------------------------------
#task 2 - type casting
num1 = "10"
num2 = "20"
#convert string into integer 
sum_result = int(num1) + int(num2)
print("Sum after type casting is :",sum_result)

#--------------------------------------------------
#user input and type conversion 
current_age=int(input("Enter your age :"))
future_age= current_age + 5

print("After 5 years ypu will be",future_age,"years old!")

#--------------------------------------------------
print ("practice--------------------------------------------------------------")
number1 = int(input("Enter 1st no. :"))#for integer multiplication
number2 = float(input("Enter 2nd no. :"))#for floating point result division

result_mul= number1 * number2 
result_div = number1 / number2

print("Multiplication of the no.s are :",result_mul)
print("Division of the no.s are :",result_div)