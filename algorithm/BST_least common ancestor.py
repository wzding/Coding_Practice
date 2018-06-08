# question4  Find the least common ancestor between two nodes on a binary search tree.
# https://discuss.leetcode.com/topic/18387/3-lines-with-o-1-space-1-liners-alternatives
def question4(T, r, n1, n2):
    T_dict = dict()
    for row in xrange(len(T)):
        if T[row].count(1) == 1: # a node with one child
            T_dict[row] = T[row].index(1)
        elif T[row].count(1) == 2:  # a node with two children
            indices = [i for i, j in enumerate(T[row]) if j == 1]
            T_dict[row] = indices
    while (r - n1) * (r - n2) > 0:  # if both nodes are on the same side of the root
        r = (T_dict[r][0], T_dict[r][1])[n1 > r] # choose which side the two nodes belong
    return r

print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 4)
# 3
print question4([[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [1, 0, 0, 1],
                 [0, 1, 0, 0]],
                 2,
                 0,
                 1)
# 0 
print question4([[0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0]],
                 3,
                 2,
                 1)
# 1

# The idea is to walk down from the whole tree's root as long as both n1 and n2 are in the same sub tree, meaning that their values are both smaller or both larger than root's. If (r - n1) * (r - n2) > 0, then both n1 and n2 are on one side of the root. Then we updated the root to either its left or right node depending on the value of n1 and n2. For example, if n1 > r, we set the current root to the right node of r. We created a new dictionary (T_dict) to store the children of a certain node. If a node does not have a child, we ignored this node. We chose a dictionary because the value of a dictionary is very flexible, it could be a string or a list. This iterative method has O(1) space complexity, its time complexity is O(n) in the worst case. 