app = str(input("Please input a string\n:"))
newelements = ""

for elements in app:
    if elements.islower():
        newelements+= elements.upper()
    elif elements.isupper():
        newelements+=elements.lower()
    else:
        newelements +=elements
print("The new string is",newelements)