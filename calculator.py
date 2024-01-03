# Program for calculation between two numbers

# Taking input from the user
print("Enter two numbers for calculation")
a=float(input("Enter 1st number\t"))
b=float(input("Enter 2nd number\t"))

# Taking input for operator
print("Select operator from 1-6")
print("1 for +")
print("2 for -")
print("3 for *")
print("4 for /(for a divided by b & b should not equal to 0)")
print("5 for %")
print("6 for **(for a raised to power b)")
choice=int(input(""))

# Giving output
match choice:
   case 1:print("Result:",a+b)
   case 2:print("Result:",a-b)
   case 3:print("Result:",a*b)
   case 4:print("Result:",a/b)
   case 5:print("Result:",a%b)
   case 6:print("Result:",a**b)
   case _:print("Invalid operator selected")