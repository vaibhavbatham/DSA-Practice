class Solution:
    def sortString(self, s):
        s_arr = list(s)
        s_arr.sort()
        return "".join(s_arr)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict1 ={}

        for s in strs:
            key = self.sortString(s)
            if key in dict1:
                dict1[key].append(s)
            else:
                dict1[key] = [s]
        
        return list(dict1.values())