# Break statement is used to exit the Loop
# Continue statement is used to skip the iteration

no=int(input("Enter a number to print table: "))
print("The table of ", no,"is")
i=1
for i in range(17):
    if(i==10):
        break
    print(no," x ",i+1, "=", no*(i+1))
     