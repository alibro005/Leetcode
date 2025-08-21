class Solution:
    def merge(self, nums, l, mid, r):

        a = nums[l : mid + 1]
        b = nums[mid + 1 : r + 1]

        # for i in range(l, mid + 1):
        #     a.append(nums[i])
        # for i in range(mid + 1, r + 1):
        #     b.append(nums[i])

        n, m = len(a), len(b)
        i, j, k = 0, 0, l

        while i < n and j < m:
            if a[i] <= b[j]:
                nums[k] = a[i]
                i += 1
            else:
                nums[k] = b[j]
                j += 1
            k += 1
        if i < n:
            while i < n:
                nums[k] = a[i]
                i += 1
                k += 1
        if j < m:
            while j < m:
                nums[k] = b[j]
                j += 1
                k += 1

    def mergeSort(self, nums, l, r):

        if l >= r:
            return

        mid = (l + r) // 2

        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)

        self.merge(nums, l, mid, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1

        self.mergeSort(nums, l, r)

        return nums
