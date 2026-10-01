class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
      
        curr = 1

        for i in range (1 , len(nums)):
            
            if nums[i-1] != nums[i]:
                nums[curr] = nums[i]
                curr +=1

        return curr