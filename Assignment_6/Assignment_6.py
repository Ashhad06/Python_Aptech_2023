def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def calculator():
    A=input("Enter what do you want to do? (+,-,*,/) : ")
    Num1 = int(input("Enter Your first number :"))
    Num2 = int(input("Enter Your second number"))
    if A== "+":
        result= add(Num1,Num2)
    elif A== "-":
        result= subtract(Num1,Num2)
    elif A== "*":
        result= multiply(Num1,Num2)
    elif A== "/":
        result= divide(Num1,Num2)
    else:
        print("Invalid! Pls try again")
    print("Your result is :"+ str(result))
calculator()
