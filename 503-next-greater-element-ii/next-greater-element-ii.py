class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        arr = nums+nums
        stack = []
        ans =[-1] * len(arr)

        for i in range(len(arr)-1 , -1 ,-1):

            while len(stack) > 0 and stack[-1] <= arr[i]:
                stack.pop()

            if len(stack)!=0:
                ans[i] = stack[-1]

            stack.append(arr[i])

            
        return ans[:len(ans)//2 ]