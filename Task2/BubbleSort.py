x = input("Enter list: ")
lst = [int(a) for a in x.split(",")]

n = len(lst)
for i in range(n - 1):
    for item in range(n - i - 1):
        if lst[item] > lst[item + 1]:
            lst[item], lst[item + 1] = lst[item + 1], lst[item]

print("Sorted list:", lst)
