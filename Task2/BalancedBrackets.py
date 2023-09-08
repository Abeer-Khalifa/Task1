x=input("")
if (x[0]==")") or (x[-1]=="("):
    print ("no")
else:
    a=x.count("(")
    b=x.count(")")
    if(a==b):
        print("yes")
    else:
        print("no")
