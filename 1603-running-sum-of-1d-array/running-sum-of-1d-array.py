class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        list1 = []
        sum1 = 0
        for i in range (len(nums)):
            sum1 += nums[i]
            list1.append(sum1)
        
        return list1