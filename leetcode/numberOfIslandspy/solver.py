file1 = open('Year2023/leetcode/numberOfIslandspy/data.txt', 'r')
lines = file1.readlines()

inputArray = []

for line in lines:
    line = line.strip()
    # print(line.split())
    # [c for c in s]
    inputArray.append([c for c in line])


def findIfNeighborsAreIsland(x,y):

    if(x > 0 and inputArray[x - 1][y] != '.'):
        return inputArray[x-1][y]
    if(y > 0 and inputArray[x][y - 1] != '.'):
        return inputArray[x][y - 1]
    return '.'



print(inputArray[0][1])

count = 0


for (i, line) in enumerate(inputArray):
    for (j, el) in enumerate(line):
        if(el == 'x'):
            neighborValue = findIfNeighborsAreIsland(i,j)
            if(neighborValue == '.'):
                count += 1
                inputArray[i][j] = count
            if(neighborValue != '.'):
                inputArray[i][j] = neighborValue

print(inputArray)
print(count)