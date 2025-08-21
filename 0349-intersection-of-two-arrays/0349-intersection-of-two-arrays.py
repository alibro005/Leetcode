class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        result = []

        for i in nums1:
            dict1[i] = dict1.get(i, 0) + 1
        for i in nums2:
            dict2[i] = dict2.get(i, 0) + 1

        for key in dict1:
            if key in dict2:
                result.append(key)
        return result
