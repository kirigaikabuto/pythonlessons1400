a = input("a=")
b = input("b=")
aint = int(a)
bint = int(b)
if aint % bint:
    print(f"{aint} делиться на {bint} без остатака")
else:
    print(f"{aint} делится на {bint} с остатком")
