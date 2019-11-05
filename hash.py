storage = [[] for x in range(15)]


def hash(key):
    index = sum(list(map(ord, key)))
    index = sum(list(map(int, str(index))))
    return index % len(storage)


def set_value(key, value):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
            i[1] = value
            break
    else:
        storage[index].append([key, value])


def del_value(key):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
             storage[index].remove(i)
            break


def get_value(key):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
            return i[1]


print(storage)

set_value('abc', 1)
set_value('abc', 100)

set_value('xyz', 2)
set_value('xyz', 200)

set_value('ert', 3)
set_value('ert', 300)

print(storage)

del_value('ert')

print(get_value('abc'))
print(get_value('xyz'))

print(storage)
