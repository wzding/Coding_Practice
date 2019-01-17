"""
https://www.lintcode.com/problem/majority-element/description
Moore's voting algorithm -- if the majority does exist, we can always find
another value to pair with each instance of majority element we've seen so far
and this part cancel out.
"""

class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # Moore's voting algorithm
        ans = None
        count = 0
        for num in nums:
            if count == 0:
                ans = num
            if num == ans:
                count += 1
            else:
                count -= 1
        return ans
