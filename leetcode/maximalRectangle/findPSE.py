# purpose of this function is to find the previous smallest element
# and return the index of that element
# if there is no previous smallest element then return self index
#
def findPSE(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [0]

    answer = [0]
    stack = [0]

    for i in range(1, len(array)):
        top = len(stack) - 1
        if array[stack[top]] < array[i]:
            answer.append(stack[top])
            stack.append(i)
        elif(array[stack[top]] >= array[i]):
            while top >= 0 and array[stack[top]] >= array[i]:
                stack.pop()
                top = len(stack) - 1
            stack.append(i)
            answer.append(stack[top])
    return answer
def findNSE(array):
    array = array[::-1]
    answer = list(map(lambda x: len(array) - x -1,findPSE(array)))
    return answer[::-1]



# findPSE([12,4,5,2,9])
# findPSE([8,4,2,2,9])
# findPSE([1,2,3,4,5])
# findNSE([5,4,3,2,1])
# findNSE([12,3,4,5,6])
arr = [3, 1, 3, 2, 2]
pseArr = findPSE(arr)
nseArr = findNSE(arr)
print(arr)
print(pseArr, nseArr)

countRectangle = 0
for i,e in enumerate(arr):
    # print(i,e)
    lMin = pseArr[i]
    rMin = nseArr[i]

    if lMin == i:
        lMin = -1
    if rMin == i:
        rMin = len(arr)

    tempAnswer = e * (rMin - lMin - 1)
    print(tempAnswer, i, e)
    if tempAnswer > countRectangle:
        countRectangle = tempAnswer
print(countRectangle)
