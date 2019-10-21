from random import randint
a = [randint(3, 33) for x in range(10)]

j = len(a) - 1
while j > 0:
    m = 0
    for i in range(1, j + 1):
        if a[i] > a[m]:
            m = i
    a[m], a[j] = a[j], a[m]
    j -= 1

print(a)
