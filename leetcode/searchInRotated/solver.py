import math

class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while True:

            # if nums[left] == target:
            #     return left
            # if nums[right] == target:
            #     return right

            tempBefore = str(left) + str(right)
            mid = math.floor((right + left) / 2)
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

            if str(left) + str(right) == tempBefore:
                break


        print(left, right, '='*8)

        return -1

s = Solution()
print(s.search([8,9,0,1,2,3,4,5], 4))
print(s.search([1,2,3,4,5,6,7,8], 0))
# print(s.search([1,2,3,4,5,6,7,8,0], 1))
# print(s.search([1,2,3,4,5,6,7,8,0], 2))
# print(s.search([1,2,3,4,5,6,7,8,0], 3))
# print(s.search([1,2,3,4,5,6,7,8,0], 4))
# print(s.search([1,2,3,4,5,6,7,8,0], 5))
# print(s.search([1,2,3,4,5,6,7,8,0], 6))
# print(s.search([1,2,3,4,5,6,7,8,0], 7))
# print(s.search([1,2,3,4,5,6,7,8,0], 8))
# print(s.search([1,2,3,4,5,6,7,8,0], 99))
# print(s.search([1,2,3,4,5,6,7,0], 4))
# print(s.search([1,2,3,4,5,6,7,0], 3))
