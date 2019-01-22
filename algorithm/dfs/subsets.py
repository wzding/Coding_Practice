# iterative method
class Solution:
    def subsets(self, nums):
        result = []
        n = len(nums)
        nums.sort()

        # 1 << n is 2^n
        # each subset equals to an binary integer between 0 .. 2^n - 1
        # 0 -> 000 -> []
        # 1 -> 001 -> [1]
        # 2 -> 010 -> [2]
        # ..
        # 7 -> 111 -> [1,2,3]
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    subset.append(nums[j])
            result.append(subset)
        return result
