# two ways
"""
1. 实现__lt__方法:
以Interval区间为例，在定义该类时，重写其中的__lt__方法，使得Interval类可以进行大小比较，这样也可实现自定义的排序
这样，在其他地方就可以直接对Interval对象的大小进行比较。完整的测试方法如下
"""
class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    # 以下为重写的__lt__方法
    def __lt__(self, other):
        # 当两个Interval比较大小时，直接比较它们的left属性
        return self.left < other.left


# Interval类如上

if __name__ == "__main__":
    A = []
    A.append(Interval(1, 7))
    A.append(Interval(5, 6))
    A.append(Interval(3, 4))
    print("Before sort:")
    for i in A:
        print("({},{})".format(i.left, i.right))

    # 由于定义了__lt__，方法，此处可以直接调用sort方法进行升序排序
    A.sort()

print("After sort:")
    for i in A:
        print("({},{})".format(i.left, i.right))

"""
2. 定义key函数
可以给sort方法传入一个key函数，表示按照什么标准来对元素进行排序，仍以上面的例子为例:
"""
# 要传给sort函数的key方法，表示按照interval.left进行排序
def IntervalKey(interval):
    return interval.left

A = []
A.append(Interval(1, 7))
A.append(Interval(5, 6))
A.append(Interval(3, 4))
A.sort(key=IntervalKey)
