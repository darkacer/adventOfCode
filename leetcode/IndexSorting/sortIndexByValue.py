# given an array sort its index array by its values

arr = [12,10,19,15,9,7,20,11,10]
indexArr = [i for i in range(len(arr))]
print(indexArr)
def partitionArrayIndex(start, end):
    pivotIndex = end

    leftArrIndex = []
    rightArrIndex = []

    for i in range(start,end):
        if arr[indexArr[i]] <= arr[indexArr[pivotIndex]]:
            leftArrIndex.append(indexArr[i])
        else:
            rightArrIndex.append(indexArr[i])
    print(pivotIndex, leftArrIndex, rightArrIndex)
    finalArr = []

    for i in leftArrIndex:
        finalArr.append(i)
    finalArr.append(pivotIndex)
    for i in rightArrIndex:
        finalArr.append(i)

    print("finalArr",finalArr)

    counter = 0
    for i in range(start, end+1):
        indexArr[i] = finalArr[counter]
        counter += 1

    print(indexArr)

    return len(leftArrIndex)



    # print(start)


# partitionArray(indexArr, len(arr) - 1)

print(partitionArrayIndex(0,8))
