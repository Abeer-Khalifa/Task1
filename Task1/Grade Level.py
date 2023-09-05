letters=0
Sentences=0
words=1
paragraph=input("Enter text: ")
for i in paragraph:
    if i not in (" ", "," ,"." ,"?" ,"!" ,"'"):
        letters+=1
    if i in (".","!","?"):
        Sentences+=1
    if i==(" "):
        words+=1
L=(letters/words)*100
S=(Sentences/words)*100
Grade=(0.0588*L)-(0.296*S)-15.8
print("Grade "+str(round(Grade)))