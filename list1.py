list1=[45,76,98,"Gautam",True,66,576,"Task"]
# print(list1)
# print(len(list1))
# print(type(list1))
# print(list1[3])

print(list1[0:8:2])

# i=0
# for i in list1:
#     if(i==98):
#         print(i,"is found")
    
a=int(input("Enter element to check in list: "))
if a in list1:
    print("Yes")
else :
    print("No")