class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        dit ={}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in dit:
                return [dit[rem] , i]

            dit[nums[i]] = i    

