# Program for using list comprehension

a=int(input("Enter no. of terms: "))
lst=[i for i in range(a+1) if i%5==0]
print(lst)