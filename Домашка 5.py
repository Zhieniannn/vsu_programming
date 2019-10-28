import collections
names = {
    "Arsenii": ["Danil", "Jecka"],
    "Danil": ["Denchick1", "Albert"],
    "Jecka": ["Dima", "David"]
}


def notahuman(a):
    return not len(a) % 2 and a[0] == "D"


c = []
b = collections.deque(names["Arsenii"])
while names:
    d = b.popleft()
    if d not in c:
        if notahuman(d):
            print(d)
            break
            b += names.get(d, [])
        c.append(d)
