class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = dict()
        freq2 = dict()

        n = len(nums1)
        m = len(nums2)

        result = []

        for i in range(n):
            freq1[nums1[i]] = freq1.get(nums1[i], 0) + 1

        for i in range(m):
            freq2[nums2[i]] = freq2.get(nums2[i], 0) + 1

        for num in freq1:
            if num in freq2:
                count = min(freq1[num], freq2[num])

                for _ in range(count):
                    result.append(num)

        return result

        print(freq1)
        print(freq2)
