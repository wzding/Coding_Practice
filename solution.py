# question1 
def question1(s,t): 
    if s.find(t) == -1:
        return False
    return True

print question1("Udacity","da")
print question1("Udacity","Udacity")
print question1("Udacity","ad")

def question2(a):
    res = ""
    for i in xrange(len(a)):
        temp = palindromic(a,i,i)
        if len(temp) > len(res):
            res = temp
        
        temp = palindromic(a,i,i+1)
        if len(temp) > len(res):
            res = temp  
    return res

def palindromic(string, start, end):
    while start >= 0 and end < len(string) and string[start] == string[end]:
        start -= 1
        end += 1
    return string[start+1:end]

print question2("abcdd")
print question2("abcbdd")
print question2("abcccba")

# question3
def sort_list(G):
    list0 = []
    for i in G:
        for j in G[i]:
            list0.append((i,j[0],j[1]))

    list0 = sorted(list0,key=lambda item:item[2])
    return list0

def find_prt(parent,i):
    if parent[i] == i:
        return i
    return find_prt(parent,parent[i])

def union(parent,rank,x,y):
    if rank[x] < rank[y]:
        parent[x] = parent[y]
    elif rank[x] > rank[y]:
        parent[y] = parent[x]
    else:
        parent[y] = parent[x]
        rank[x] += 1    
        
def question3(G):
    list_sort = sort_list(G)
    result = dict() ; parent = dict() ; rank = dict()
    i = 0 ; e = 0
    
    for node in G:
        parent[node] = node
        rank[node] = 0

    while e < len(parent) - 1:
        u,v,w = list_sort[i]
        i = i +1
        x = find_prt(parent,u)
        y = find_prt(parent,v)
        
        if x!= y:
            e = e + 1
            result[u] = [(v,w)]
            union(parent,rank,x,y)
    return result

G = {'A': [('B', 2)],'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
print question3(G)
G = {'A': [('B', 2)],'B': [('A', 2), ('C', 1)], 'C': [('B', 1)]}
print question3(G)
G = {'0': [('1', 10),('2',6),('3',5)],'1': [('0', 10),('3', 15)], \
     '2': [('3', 4),('0',6)], '3':[('0', 5),('1',15)]}
print question3(G)

# question4
def question4(T, r, n1, n2):
    T_dict = dict()
    for row in xrange(len(T)):
        if T[row].count(1) == 1:
            T_dict[row] = T[row].index(1)
        elif T[row].count(1) == 2:
            indices = [i for i, j in enumerate(T[row]) if j == 1]
            T_dict[row] = indices
    while (r - n1) * (r - n2) > 0:
        r = (T_dict[r][0], T_dict[r][1])[n1 > r]
    return r

print question4([[0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]],
                 3,
                 1,
                 4)
print question4([[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [1, 0, 0, 1],
                 [0, 1, 0, 0]],
                 2,
                 0,
                 1)
print question4([[0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0]],
                 3,
                 2,
                 1)

# question5
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def question5(self,ll, m):
        main_pt = ll
        ref_pt = ll
        
        count = 0
        if ll is not None:
            while count < m:
                if ref_pt is None:
                    return
                ref_pt = ref_pt.next
                count += 1
        
        while ref_pt is not None:
            main_pt = main_pt.next
            ref_pt = ref_pt.next
        return main_pt.data

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
print question5(list0.head,2)

list1 = linkedlist()
list1.push(2)
list1.push(1)
list1.push(6)
print question5(list1.head,1)

list2 = linkedlist()
list2.push(2)
list2.push(1)
list2.push(6)
print question5(list2.head,4)