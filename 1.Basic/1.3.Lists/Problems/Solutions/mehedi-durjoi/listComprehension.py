x = int(input())
y = int(input())
z = int(input())
n = int(input())

def find_list(x, y, z, n):
    lst = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                tmpLst = [i, j, k]
                if(sum(tmpLst) != n):
                    lst.append(tmpLst)
    return lst

print(find_list(x, y, z, n))
