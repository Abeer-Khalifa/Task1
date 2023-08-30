n=0
while n>8 or n<1:
    n=int(input("Input: "))
    if n>8:
        print("Number must be smaller than or equal to 8")
    elif n<1:
        print("Number must be greater than or equal to 1")
for i in range (n):
    print (" "*(n-i-1) + "#"*(i+1) +"  " + "#"*(i+1) )