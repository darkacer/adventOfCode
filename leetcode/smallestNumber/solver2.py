num = '1234512'

k = 3

num = list(num)

pointer = 1

def removeLeadingZerosConvertToString(array):
    
    sumSoFar = 0
    string = ''
    for i in array:
        sumSoFar += int(i)
        if sumSoFar > 0:
            string += i
    if sumSoFar == 0:
        return '0'
    return string

while True:
    # print('pointer at', pointer, num, k)
    if num[pointer - 1] > num[pointer] and k > 0:
        num[pointer - 1] = 'x'
        k -= 1
        # print('marking here 0', pointer - 1)
        tempPointer = pointer - 2
        while tempPointer >= 0 and k > 0:
            # print('inside while', tempPointer)
            if num[tempPointer] == 'x':
                tempPointer -= 1
                continue
            if num[tempPointer] > num[pointer] and k > 0:
                k -= 1
                # print(k)
                num[tempPointer] = 'x'
                # print('marking here 1', tempPointer)
                tempPointer -= 1
            else:
                break
        
        
    pointer += 1

    if pointer >= len(num) or k < 0:
        break

num = list(filter(lambda x : x != 'x', num))
# answer = "".join(num)
answer = removeLeadingZerosConvertToString(num)

if k > 0:
    answer = answer[:(k * -1)]
    if answer == '':
        answer = '0'

print(len(num), k)
print(answer)