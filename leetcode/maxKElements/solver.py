class PriorityQueue:

    queue = []
    indexes = []
    size = 0
    minAt = 0

    def __init__(self, size):
        self.size = size

    def push(self, element, index):
        print('pushing', element, self.size)

        if len(self.queue) < self.size:
            self.queue.append(element)
            self.indexes.append(index)
        else:
            print(element)
            self.queue[self.minAt] = element
            self.indexes[self.minAt] = index

        # find new min
        for i in range(0,len(self.queue)):
            if self.queue[i] < self.queue[self.minAt]:
                self.minAt = i

    def pop(self):
        print('popping')



arr = [1,11,2,18,3,4,5,6,7,14]
k = 4

queue = PriorityQueue(k)


for i in range(len(arr)):
    queue.push(arr[i],i)

print(queue.queue)
print(queue.indexes)