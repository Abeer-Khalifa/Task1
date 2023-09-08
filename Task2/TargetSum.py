def finder(target,lst,first=0,last=None):
    if last is None:
        last=len(lst)-1
    if first>=last:
        return "no"
    if lst[first]+lst[last] is target:
        return f"yes, {target}={lst[first]}+{lst[last]}"
    elif lst[first]+lst[last] <target:
        return finder(target,lst,first+1,last)
    elif lst[first]+lst[last]>target:
        return finder(target,lst,first,last-1)
    else:
        return "no"

x = input("Enter list: ")
lst = [int(a) for a in x.split(" ")]
lst.sort()
target = int(input("Enter target number: "))
print(finder(target,lst))

