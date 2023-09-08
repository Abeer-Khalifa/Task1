x=input("Enter first string: ")
y=input("Enter second string: ")
x=sorted(x)
y=sorted(y)
if x==y:
    print("They are anagrams")
else:
    print ("The strings aren't anagrams")