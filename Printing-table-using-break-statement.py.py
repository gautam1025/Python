no=int(input("Enter a number to print table: "))
print("The table of ", no,"is")
i=1
for i in range(12):
    print(no," x ",i+1, "=", no*(i+1))
    if(i==10):
        break 