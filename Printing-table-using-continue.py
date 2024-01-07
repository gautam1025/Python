# Break statement is used to exit the Loop
# Continue statement is used to skip the iteration

no=int(input("Enter a number to print table: "))
print("The table of ", no,"is")
i=1
for i in range(15):
    if(i+1==10):
        print("Skipped iteration")
        continue
    print(no," x ",i+1, "=", no*(i+1))