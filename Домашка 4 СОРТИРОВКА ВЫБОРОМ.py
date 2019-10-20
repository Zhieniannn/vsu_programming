from random import random
a = [0] * 10
for i in range(10):
    a[i] = int(random() * 100)
print(a)

j = 9
while j > 0:
    m = 0
    for i in range(1, j + 1):
        if a[i] > a[m]:
            m = i
    a[m], a[j] = a[j], a[m]
    j -= 1

print(a)
