def test(l: list[int], x: int):
    l.append(x)

def removefrom(l: list, index: int):
    l.pop(index)

mylist = [1, 2, 69]
test(mylist, 3)

print(mylist)

removefrom(mylist, 2)
print(mylist)

