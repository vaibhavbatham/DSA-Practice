class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dict1 = {}

        for i in range  (len(numbers)):

            rem = target - numbers[i]

            if rem in dict1:
                return[dict1[rem] , i +1]

            dict1[numbers[i]] = i+1