n=int(input("Enter the amount in Egyptian Pounds: "))
Hundreds2=n//200
n=n%200
Hundreds=n//100
n=n%100
fifties=n//50
n=n%50
twenties=n//20
n=n%20
tens=n//10
n=n%10
fives=n//5
n=n%5
one=n//1
print(str(Hundreds2)+"x200 + "+str(Hundreds)+"x100 + "+str(fifties)+"x50 + "+str(twenties)+"x20 + "+str(tens)+"x10 + "+str(fives)+"x5 + "+str(one)+"x1")