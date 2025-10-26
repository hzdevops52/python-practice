print("Hello")
name = "hassan"
print("my name is",name)

#if else if statement

day = input("enter the day :").lower()

if day == "saturday" or day == "sunday":
    print("its a weekend")
else:
    print("its not a weekend")


#simple calculator

num1 = float(input("enter the first nbr:"))
num2 = float(input("enter the first nbr:"))

choice = input("enter the choice + , - , / , * , % : ")

if choice == "+":
    sum = num1 + num2
    print("sum of two nbrs : ",sum)
elif choice == "-":
        diff = num1 - num2
        print("diff of two nbrs :",diff)
elif choice == "*":
        multiple = num1 * num2
        print("multiple of two nbrs :",multiple)
elif choice == "/":
        division = num1 / num2
        print("division of two nbrs :",division)
elif choice == "%":
        remainder = num1 % num2
        print("remainder of two nbrs :",remainder)
else:
    print("invalid choice")


#loops
#range()

print(range(10))

for i in range(10):
        print(i)

for i in range(0,20,2):
        print(i)


#variables

num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

sum = num_1 + num_2
print("Sum of two numbers is",sum)

diff = num_1 - num_2
print("Difference of two numbers is",diff)

product = num_1 * num_2
print("Product of two numbers is",product)

quotient = num_1 / num_2
print("Quotient of two numbers is",quotient)

remainder = num_1 % num_2
print("Remainder of two numbers is",remainder)

#practice

name = input("enter your name :")
print("welcome",name)

nbr1 = int(input("enter first nbr :"))
nbr2 = int(input("enter second nbr :"))

print(type(nbr1))
print(type(nbr2))

output = nbr1 + nbr2
print("addition is",output)

output = nbr1 - nbr2
print("subtraction is",output)

output = nbr1 / nbr2
print("division is",output)

output = nbr1 * nbr2
print("multiple is",output)

output = nbr1 % nbr2
print("remainder is",output)

