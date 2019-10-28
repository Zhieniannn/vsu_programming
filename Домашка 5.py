import collections
names = {
    "Arsenii": ["Danil", "Jecka"],
    "Danil": ["Denchick", "Albert"],
    "Jecka": ["Dima", "David"]
    }
def notahuman(a):
    if not len(a) % 2 and a[0] == "D":
        return True
    return False
c = []
b = collections.deque(names["Arsenii"])
while names:
    d = b.popleft()
    if d not in c:
        if notahuman(d):
            print(d)
            break
        else:
            b += names[d]
        c.append(d)
