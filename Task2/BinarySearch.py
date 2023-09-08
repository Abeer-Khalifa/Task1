def binSearch(target,lst,first=0,last=None):
    #Middle,first and last are indices carrying th values
    if last is None:
        last=len(lst)-1
    while last>=first:
        middle=(first+last)//2
        if lst[middle]==target:
            return f"Found at {middle}"
        elif target<lst[middle]:
            return binSearch(target,lst,0,middle-1)
        elif target>lst[middle]:
            return binSearch(target,lst,middle+1,None)
    return "Not found" #implemented if while breaks without having given out a return

input_lst=input("Enter sorted list: ")
lst=[int (a) for a in input_lst.split(",")]
target=int(input("Enter target: "))
print(binSearch(target,lst))