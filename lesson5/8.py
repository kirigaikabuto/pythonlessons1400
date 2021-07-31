arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
n = int(input("число:"))
index = arr.index(n)
arr.pop(index)
print(arr)
