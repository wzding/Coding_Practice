# https://www.lintcode.com/problem/recover-rotated-sorted-array/description
class Solution:
    """
        @param nums: An integer array
        @return: nothing
        """
    def recoverRotatedSortedArray(self, nums):
        # find peak
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                self.reverse(nums, 0, i)
                self.reverse(nums, i+1, n-1)
                self.reverse(nums, 0, n-1)
    
    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -=1

# https://www.lintcode.com/problem/rotate-string/description
class Solution:
    """
        @param str: An array of char
        @param offset: An integer
        @return: nothing
        """
    def rotateString(self, s, offset):
        # write your code here
        n = len(s)
        if offset == 0 or n == 0:
            return
        
        if offset > n:
            offset = offset % n
        
        idx = n - 1 - offset
        self.reverse(s, 0, idx)
        self.reverse(s, idx + 1, n - 1)
        self.reverse(s, 0, n-1)

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
