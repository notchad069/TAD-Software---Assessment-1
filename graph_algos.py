#implementing dfs,bfs,dijkastra's and mst on a graph and trace it

#let's say we're given the adjacency list - {0: [1, 3], 1: [2], 3: [4, 6, 7], 4: [2, 5], 5: [2]}

adj_list = {
    0: [(1, 2), (3, 5)],
    1: [(2, 1)],
    3: [(4, 3), (6, 2), (7, 1)],
    4: [(2, 4), (5, 6)],
    5: [(2, 2)]
}

def trace_log(action, trace_list): #this function would record the traversal 
    print(action)
    trace_list.append(action)
    

#dfs

def dfs(adj_list):
    trace = [] #creatin an empty list for tracing
    source = 0 #startin from 0 which is the source node
    visited = set() #this set is needed to make sure we dont revisit the values that are already seen
    stack = [source] #to process erythin
    trace_log(f"startin from node {source}", trace)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            trace_log(f"visited {node}", trace)
            for neighbor, _ in reversed(adj_list.get(node, [])):
                if neighbor not in visited:
                    trace_log(f"push {neighbor} to stack", trace)
                    stack.append(neighbor)

    print("here's the trace:")
    for step in trace:
        print(step)

#bfs

from collections import deque

def bfs(adj_list):
    trace = []
    source = 0
    visited = set([source])
    queue = deque([source])
    trace_log(f"startin from {source}", trace)

    while queue:
        node = queue.popleft()
        trace_log(f"visited {node}", trace)
        for neighbor, _ in adj_list.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                trace_log(f"enqueue {neighbor}", trace)

    print("here's the trace:")
    for step in trace:
        print(step)
                
def dijkstra(adj_list):
    
    trace = [] 
    dist = {} 
    for u in adj_list: #initializing the dist of all nodes to infinity
        dist[u] = float('inf')
        for v, _ in adj_list[u]:
            if v not in dist:
                dist[v] = float('inf')

    dist[0] = 0 #startin from the source node, we're gonna find the shortest dists to other nodes from the source node
    visited = set()
    trace_log(f"startin from node 0", trace)

    while len(visited) < len(dist): #the loop ends when all the nodes in dist ends up in visited
        min_node = None
        min_dist = float('inf')
        for node in dist:
            if node not in visited and dist[node] < min_dist: #updatin those two once this satisfies
                min_node = node
                min_dist = dist[node]

        if min_node is None:
            break

        visited.add(min_node)
        trace_log(f"visitin node {min_node} with current distance of {min_dist}", trace)

        for neighbor, weight in adj_list.get(min_node, []):#updatin all the nodes in one go by checkin the neighbors of min_node and updatin their distances too
            if neighbor not in visited:
                new_dist = dist[min_node] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    trace_log(f"updatin distance for node {neighbor} to {new_dist}", trace)

    print("here's the trace:")
    for step in trace:
        print(step)
#mst

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # they belong to the same group
        self.parent[py] = px  
        return True


def kruskal_mst(adj_list):
    trace = []
    edges = [] #we're bouta create a tuple that contains the weight of the edge and the two nodes that the edge connects
    for u in adj_list:
        for v, w in adj_list[u]:
            edges.append((w, u, v))

    edges.sort() #we're sorting the edge list here
    nodes = set() #this set will hold all the nodes
    for _, u, v in edges:
        nodes.update([u, v])

    dsu = DSU(max(nodes) + 1)
    mst = [] #we'll enter the edges that would be used to take that path 
    total_weight = 0 #initiatin the total weight to zero so that we could get the total weight at the end of the function
 
    for w, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            trace_log(f"add edge {u} -> {v} (weight {w})", trace)
        else:
            trace_log(f"skip edge {u} -> {v} (would form a cycle)", trace)

    print("here's the trace:")
    for step in trace:
        print(step)
    print(f"total weight: {total_weight}")
    return mst, total_weight 


#prim's mst

def prim_mst(adj_list):
    trace = []
    all_nodes = set(adj_list.keys()) #adding all the nodes to a set
    for neighbors in adj_list.values():
        for node, _ in neighbors:
            all_nodes.add(node)

    visited = set()
    source = 0
    visited.add(source)
    mst = []
    total_weight = 0

    trace_log(f"startin from node {source}", trace)

    while len(visited) < len(all_nodes):
        min_edge = None
        min_weight = float('inf')

        for u in visited:  # findin the minimum weight edge from visited to unvisited
            for v, w in adj_list.get(u, []):
                if v not in visited and w < min_weight:
                    min_edge = (u, v, w)
                    min_weight = w

        if min_edge is None:
            break

        u, v, w = min_edge
        visited.add(v)
        mst.append((u, v, w))
        total_weight += w
        trace_log(f"add edge {u} -> {v} (weight {w})", trace)

    print("here's the trace")
    for step in trace:
        print(step)
    print(f"total weight: {total_weight}")

        
    

if __name__ == "__main__":
    print("dfs")
    dfs(adj_list)
    print('\n')
    
    print("bfs")
    bfs(adj_list)
    print('\n')
    
    print("dijakstra")
    dijkstra(adj_list)
    print('\n')

    print("kruskal's mst")
    mst,weight = kruskal_mst(adj_list)
    for u,v,w in mst:
        print(f"{u} -> {v} (weight of {w})")
    print(f"total weight is : ",weight)
    print('\n')

    print("prim's mst")
    prim_mst(adj_list)
