class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2 :
            return len(nums)

        curr = 2
        for i in range(2 , len(nums)):
            if nums[i] != nums[curr-2]:
                nums[curr] = nums[i]
                curr +=1 

        return curr
