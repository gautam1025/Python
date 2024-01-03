name="Gautam gupta"
lenght=(len(name))
print(lenght)
print(name[0:4]) # including 0 but not 4
print(name[1:4]) # including 1 but not 4
print(name[:]) # gives the complete string
print(name[-8:-4])
           # OR
print(name[len(name)-8:len(name)-4])
# Both the above statements gives the same output 
# This is how the negative slicing works

