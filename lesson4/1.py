# дается 4 числа и необходимо найти недомаксимальное
a = 3
b = 4
c = 3
d = 10
maxi = 0
if a > b and a > c and a > d:
    maxi = a
elif b > a and b > c and b > d:
    maxi = b
elif c > a and c > b and c > d:
    maxi = c
else:
    maxi = d
difa = maxi - a
difb = maxi - b
difc = maxi - c
difd = maxi - d
nedomax = 0
if difa == 0:
    if difb < difc and difb < difd:
        nedomax = b
    elif difc < difb and difc < difd:
        nedomax = c
    else:
        nedomax = d
elif difb == 0:
    if difa < difc and difa < difd:
        nedomax = a
    elif difc < difa and difc < difd:
        nedomax = c
    else:
        nedomax = d
elif difc == 0:
    if difa < difb and difa < difd:
        nedomax = a
    elif difb < difa and difb < difd:
        nedomax = b
    else:
        nedomax = d
elif difd == 0:
    if difa < difb and difa < difc:
        nedomax = a
    elif difb < difa and difb < difc:
        nedomax = b
    else:
        nedomax = c
print(nedomax)
