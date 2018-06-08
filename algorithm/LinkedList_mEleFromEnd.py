# Find the element in a singly linked list that's m elements from the end
# http://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
def question5(ll, m): # use two pointers: main_pt and ref_pt
    main_pt = ll
    ref_pt = ll

    count = 0
    if ll is not None:
        while count < m:
            if ref_pt is None:
                return # if m is larger than the length of the singly linked list
            # move ref_pt to the node that is m elements from the head
            ref_pt = ref_pt.next 
            count += 1

    while ref_pt is not None:
        # move ref_pt to the end 
        # move main_pt to the node that is m elements from the end
        main_pt = main_pt.next
        ref_pt = ref_pt.next
    return main_pt.data

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedlist(object):
    def __init__(self):
        self.head = None
        
    def push(self,new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

list0 = linkedlist()
list0.push(2)
list0.push(4)
list0.push(1)
list0.push(6)
print question5(list0.head,2) # 4

list1 = linkedlist()
list1.push(2)
list1.push(1)
list1.push(6)
print question5(list1.head,1) # 2

list2 = linkedlist()
list2.push(2)
list2.push(1)
list2.push(6)
print question5(list2.head,4) # None

# In this problem, we are asked to find the element in a singly linked list that's m elements from the end. My idea is to use two pointers – reference pointer and main pointer. We initialize both reference and main pointers to head. First we move reference pointer to n nodes from head, then move both pointers one by one until reference pointer reaches end. Now the main pointer points to nth node from the end. The time complexity is O(n) where n is the length of linked list. The space complexity is O(1).
