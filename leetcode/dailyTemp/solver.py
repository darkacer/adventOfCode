class Solution:

    stack = []
    temperatures = []

    def __init__(self):
        self.stack = []
        self.temperatures = []

    def pushToStack(self, element):
        i = len(self.stack) - 1
        while i >= 0:
            if self.temperatures[self.stack[i]] < self.temperatures[element]:
                self.temperatures[self.stack[i]] = element - self.stack[i] 
                self.stack.pop()
                i -= 1
            else:
                break
        self.stack.append(element)

        # print("after element", element, "this is the stack", self.stack)
        # print(self.temperatures)
    

    def dailyTemperatures(self, temperatures):

        # temperatures.append(float('inf'))
        self.temperatures = temperatures
        inputLen = len(self.temperatures)


        for i in range(inputLen):
            # print(i)
            self.pushToStack(i)

        for i in self.stack:
            self.temperatures[i] = 0

        # self.temperatures.pop()
        # self.temperatures[-1] = 0

        print("final answer", self.temperatures)

            
        return self.temperatures

# sol = 
Solution().dailyTemperatures(
    [73,74,75,71,69,72,76,73]
)
# sol = 
Solution().dailyTemperatures(
    [30,40,50,60]
)