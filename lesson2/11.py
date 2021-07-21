a = 8
b = 4
otvet = ""
if a % b == 0:
    otvet = "Число {} делится на число {} без остатка".format(a, b)
else:
    otvet = "Число {} делится на число {} c остатком".format(a, b)
print(otvet)
