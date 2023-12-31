print("Enter three numbers to compare\n")
a=int(input("Enter 1st number\t"))
b=int(input("Enter 2nd number\t"))
c=int(input("Enter 3rd number\t"))

if(a>b):
    if(a>c):
        print("1st number is greatest")
    else:
        print("3rd number is greatest")

else:
    if(b>c):
        print("2nd number is greatest")
    else:
        print("3rd number is greatest")                
   