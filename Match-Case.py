a=input("Enter the operator: ")
match a:
    case '+':
        print("This is addition operator")
    case '-':
        print("This is subtraction operator")
    case '/':
        print("This is division operator")
    case '*':
        print("This is multiplication operator")
    case _:
        print("Invalid input\nEnter the valid operator")