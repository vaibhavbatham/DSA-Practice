class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans =[]
        for i in range(len(nums1)):
            greater = -1
            for j in range (len(nums2)):              
                if nums1[i] == nums2[j]:
                    for k in range(j+1 , len(nums2)):
                        if nums2[k] > nums2[j]:
                            greater = nums2[k]
                            break
                    break
            
            ans.append(greater)
        return ans
                