l=[44,65,88,47,96,28]
print(l)

l.append(91)   # for adding an element to list
print(l)

l.sort()   # for sorting the list
print(l)

l.reverse()  # for reverse the list
print(l)

print(l.index(88)) # for checking index of given element
print(l.count(88)) # for counting the no. of times the element occured

 # changes made in m will be copied to l
# so we have to create a copy of list using copy()
m=l.copy()
m[2]=5
print(l)

