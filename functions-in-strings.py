# Strings are immutable
a="### Gautam ### ###"

print(len(a))
print(a.upper())
print(a.lower())

print(a.rstrip("###"))
print(a.split(" "))

print(a.replace("Gautam","Harry"))
Heading="welcome to my vlog.\npls share"

print(Heading.capitalize())
print(Heading.center(40))

print(a.count("#"))
print(Heading.endswith("share"))
print(Heading.startswith("Welcome"))

print(Heading.endswith("pls"))
print(Heading.endswith("to",2,10))

str1="I'm a good boy !!!"
print(str1.find("good"))

str2="WelcomeToTheConsole456"
print(str2.isalnum())
print(str2.isalpha())
print(str2.islower())
print(str2.isupper())

str2="WelcomeToTheConsole456"
str3="WelcomeToTheConsole456\n"
print(str2.isprintable())
print(str3.isprintable())

str1="    " # whitespaces using spacebar
print(str1.isspace())
str2="      " # whitespaces using tab
print(str2.isspace())

str1="Crime Branch India"
print(str1.istitle())
str1="Crime Branch of India"
print(str1.istitle())

str5="Python is a case sensitive languauge"
print(str5.swapcase())
print(str5.title())