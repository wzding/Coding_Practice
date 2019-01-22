# 如何求一个排列是第几个排列？
class Solution:
    """
        @param A: An array of integers
        @return: A long integer
        """
    def permutationIndex(self, A):
        permutation = 1
        result = 0
        for i in range(len(A) - 2, -1, -1):
            smaller = 0
            for j in range(i + 1, len(A)):
                if A[j] < A[i]:
                    smaller += 1
            result += smaller * permutation
            permutation *= len(A) - i
        return result + 1
