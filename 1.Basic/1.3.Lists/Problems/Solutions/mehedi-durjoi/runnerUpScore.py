input()
lst = [int(x) for x in input().split()]

newLst = set(lst)
newLst.remove(max(newLst))

print(max(newLst))
