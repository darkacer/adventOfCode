# find algo
def find(el):
    print("in", el)
    if parent[el] == el:
        return el

    parent[el] = find(parent[el])
    return parent[el]
    # return find(parent[el])

def union(u,v):
    u = find(u)
    v = find(v)

    if u != v:
        parent[v] = u




# there are 9 elements in the graph
n = 9
parent = [i for i in range(n)]

union(1,2)
union(2,3)
union(4,3)
union(4,0)
union(0,5)
# union(2,3)


print(parent)
print(find(1))
print(find(2))
print(find(3))
print(parent)
