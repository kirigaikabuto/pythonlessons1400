s = input()
numbers = [int(i) for i in s.split(" ")]
chet = []
for i in numbers:
    if i % 2 == 0:
        chet.append(i)
print(chet)
