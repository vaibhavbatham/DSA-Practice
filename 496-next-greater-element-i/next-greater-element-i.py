class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []

        ans =[-1] * len(nums2)

        for i in range(len(nums2)-1 , -1 , -1):
            
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()

            if len(stack) > 0:
                ans[i] = stack[-1]

            stack.append(nums2[i])

        dic={}

        for i in range(len(ans)):
            dic[nums2[i]] = ans[i]

        res =[]

        for i in range(len(nums1)):
            res.append(dic[nums1[i]])

        return res