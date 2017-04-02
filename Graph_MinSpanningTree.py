# question3  find the minimum spanning tree within an undirected graph G
# http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/

def sort_list(G): # covert graph into a sorted list
    list0 = []
    for i in G:
        for j in G[i]:
            list0.append((i,j[0],j[1])) 

    list0 = sorted(list0,key=lambda item:item[2])
    # sort list based on weight
    return list0

def find_prt(parent,i): # find the parent node of a node
    if parent[i] == i:
        return i
    return find_prt(parent,parent[i])

def update(parent,rank,x,y): # update parent and rank
    if rank[x] < rank[y]:   
        parent[x] = parent[y]
    elif rank[x] > rank[y]:
        parent[y] = parent[x]
    else:
        parent[y] = parent[x]
        # x and y have same rank, then x's rank add 1 
        rank[x] += 1    
        
def question3(G): # apply Kruskal's MST Algorithm
    list_sort = sort_list(G) 
    result = dict() ; parent = dict() ; rank = dict()
    i = 0 ; e = 0
    
    for node in G:
        parent[node] = node 
        # initial parent is a dictionary whose value is the same as keys
        rank[node] = 0
        # initial rank is a dictionary whose value is 0 for all keys
        # root has highest rank
        
    while e < len(parent) - 1: # e is number of edges
        u,v,w = list_sort[i]
        i = i +1  # loop through the sorted list
        x = find_prt(parent,u)
        y = find_prt(parent,v)
        
        if x != y: # x != y means no cycle has formed
            e = e + 1
            result[u] = [(v,w)] 
            update(parent,rank,x,y)
    return result

G={}
print question3(G) # {}
G = {'A': [('B', 2)],'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
print question3(G)  # {'A': [('B', 2)], 'C': [('B', 5)]}
G = {'A': [('B', 2)],'B': [('A', 2), ('C', 1)], 'C': [('B', 1)]}
print question3(G)  # {'A': [('B', 2)], 'C': [('B', 1)]}
G = {'0': [('1', 10),('2',6),('3',5)],'1': [('0', 10),('3', 15)], \
     '2': [('3', 4),('0',6)], '3':[('0', 5),('1',15)]}
print question3(G)  # {'1': [('0', 10)], '0': [('3', 5)], '2': [('3', 4)]}

#   I applied Kruskal’s Minimum Spanning Tree (MST) Algorithm in this question. The steps to find the MST using Kruskal’s algorithm is as follows: 1. Sort all the edges in non-decreasing order of their weight. 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. 3. Repeat step#2 until there are (V-1) edges in the spanning tree. For step1, I converted the original graph into a list, and sorted the list based on weights. We need list here because the input graph cannot be sorted since it is a dictionary. In order to check where there is a cycle with the spanning tree formed so far, I created two dictionaries (parent and rank), and used two functions (find_prt and update). I choose dictionary as the type for parent and rank because for each node, we need the value of it parent and rank, and the order do not matter. It's easy to update the value of certain key of a dictionary. If there is no cycle after connecting node a and b, then a and b should not have the same root. I updated both parent and rank each time when there is a new node connected to the spinning tree.
#    The time complexity of this algorithm is O(ElogE) or O(ElogV), where E is the number of edges and V is the number of vertex. Sorting of edges takes O(ELogE) time. After sorting, we iterate through all edges and apply find-union algorithm. The find and union operations can take at most O(LogV) time. So overall complexity is O(ELogE) + (ELogV) time. Because E is at most V^2 and each isolated vertex is a separate component of the minimum spanning forest. If we ignore isolated vertices we obtain V ≤ 2E, so log V is also O(log E). Thus, the overall complexity is O(ElogE) or O(ElogV). 