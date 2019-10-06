a = input()
lis = []
while a:
    lis.append(a)
    a = input()
lis = sorted(lis, reverse=True)
print(''.join(lis))
