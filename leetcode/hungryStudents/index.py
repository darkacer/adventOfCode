class Solution:
    def countStudents(self, students, sandwiches):
        
        qp = 0 # queue pointer
        sp = 0 # sandwich pointer 
        incrementCounter = 0
        
        while True:

            print('before', students[qp], sandwiches[sp])

            if students[qp] == 9:
                qp = (qp + 1) % len(students)
                incrementCounter += 1
            if sandwiches[sp] == 9:
                sp = (sp + 1) % len(sandwiches)

            if students[qp] == sandwiches[sp] and students[qp] != 9:

                students[qp] = 9
                sandwiches[sp] = 9

                qp = (qp + 1) % len(students)
                sp = (sp + 1) % len(sandwiches)
                incrementCounter = 0
            
            elif students[qp] != sandwiches[sp]:
                qp = (qp + 1) % len(students)
                incrementCounter += 1
            print('after', sandwiches, students)
            
            if incrementCounter >= len(students):
                break

        return len(list(filter(lambda x: x != 9, students)))

            

# Solution.countStudents([1,1,0,0], [0,1,0,1])

sol = Solution()
# sol.countStudents([1,1,0,0], [0,1,0,1])
answer = sol.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1])

print(answer)
    