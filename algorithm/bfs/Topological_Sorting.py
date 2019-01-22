class Solution:
    """
        @param graph: A list of Directed graph node
        @return: A list of integer
        """
    def topSort(self, graph):
        node_to_indegree = self.get_indegree(graph)
        
        # bfs
        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
    return order

def get_indegree(self, graph):
    node_to_indegree = {x: 0 for x in graph}
        
        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1

    return node_to_indegree
