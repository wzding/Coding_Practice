"""
计算一个32位整数的二进制表示中有多少个1（http://www.lintcode.com/zh-cn/problem/count-1-in-binary/）。
例如32(100000)，返回1；5(101)，返回2；1023(1111111111)，返回10。
用1不断左移（左移操作可参见下文其他操作，每次和num做按位与看是否为0，不是0的话说明这一位是1。左移32次后停止。代码如下：
"""
class Solution:
    def countOnes(self, num):
        count = 0
        for i in range(32):
            if (num & (1 << i)) != 0:
                count += 1
        return count

"""
更精妙的算法
不断用num和num-1做按位与，结果直接赋给num。只要num不为0，就重复该过程。最后返回以上过程的次数即可。代码如下：
"""
class Solution:
    def countOnes(self, num):
        if num < 0:
            # Python的整数是无限长的, -1在Java/C++的32位整数中为: 11...11111 (32个1)
            # 但是在Python中为: ...1111111111111 (无限个1)
            # 因此在遇到负数时要先截断为32位
            num &= (1 << 32) - 1
        count = 0
        while num != 0:
            num &= num - 1
            count += 1
        return count
