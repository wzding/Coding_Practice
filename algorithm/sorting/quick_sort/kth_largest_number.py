class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, k, nums):
        # write your code here
        return self.quick_select(nums, k, 0, len(nums) - 1)

    def quick_select(self, nums, k, start, end):
        if start == end:
            return nums[start]
        left, right = start, end
        pivot = nums[(left + right) // 2]

        left, right = self.partition(nums, pivot, start, end)
        if start + k - 1 <= right:
            return self.quick_select(nums, k, start, right)
        if start + k - 1 >= left:
            return self.quick_select(nums, k - (left - start), left, end)
        return nums[right + 1]

    def partition(self, nums, pivot, start, end):
        left, right = start, end

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # nums[start], nums[right] = nums[right], nums[start]
        return left, right
