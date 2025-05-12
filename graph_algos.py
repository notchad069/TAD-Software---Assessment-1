#implementing dfs,bfs,dijkastra's and mst on a graph and trace it

#let's say we're given the adjacency list - {0: [1, 3], 1: [2], 3: [4, 6, 7], 4: [2, 5], 5: [2]}

adj_list = {
    0: [(1, 2), (3, 5)],
    1: [(2, 1)],
    3: [(4, 3), (6, 2), (7, 1)],
    4: [(2, 4), (5, 6)],
    5: [(2, 2)]
}

def trace():
    
    pass    

#dfs

def dfs(adj_list):
    source = 0 #startin from 0 which is the source node
    visited = set() #this set is needed to make sure we dont revisit the values that are already seen
    visited.add(source)
    stack = [source] #to process erythin
    while stack:
        node = stack.pop() 
        print(node) #processin...
        for i,_ in adj_list.get(node,[]): 
            if i not in visited:
                visited.add(i)
                stack.append(i)

#bfs

from collections import deque

def bfs(adj_list):
    source = 0
    visited = set()
    queue = deque([source])
    visited.add(source)
    while queue:
        node = queue.popleft()
        print(node)
        for i,_ in adj_list.get(node,[]):
            if i not in visited:
                visited.add(i)
                queue.append(i)
                
def dijkstra(adj_list):
    
    dist = {node : float('inf') for node in adj_list} #initializing the dist of all nodes to infinity
    
    for node,edges in adj_list.items():
        for i, _ in edges:
            if i not in dist:
                dist[i] = float('inf') #some of the neighbours might not have any connections but other nodes have connections to them. these are neglected in the first loop
    source = 0
    visited = set()
    dist[source] = 0 #startin from the source node, we're gonna find the shortest dists to other nodes from the source node
    
    while len(visited) < len(dist): #the loop ends when all the nodes in dist ends up in visited
        
        min_node = None 
        min_dist = float('inf')
        
        for i in dist:
            if i not in visited and dist[i] < min_dist: #updatin those two once this satisfies
                min_node = i
                min_dist = dist[i]

        visited.add(min_node) 
        
        for node,weight in adj_list.get(min_node,[]):#updatin all the nodes in one go by checkin the neighbors of min_node and updatin their distances too
            if node not in visited:
                new_dist = min_dist + weight
                if new_dist < dist[node]:
                    dist[node] = new_dist
    for node in dist:
        print(f"{node} : {dist[node]}")

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
    edges = [] #we're bouta create a tuple that contains the weight of the edge and the two nodes that the edge connects
    
    for u in adj_list:
        for v,w in adj_list[u]:
            edges.append([w,u,v])
            
    edges.sort() #we're sorting the edge list here
    
    nodes = set() #this set will hold all the nodes
    
    for _,u,v in edges:
        nodes.update([u,v])
    
    dsu = DSU(max(nodes) + 1 )
    mst = [] #we'll enter the edges that would be used to take that path 
    total_weight = 0 #initiatin the total weight to zero so that we could get the total weight at the end of the function
    
    for w,u,v in edges:
        if dsu.union(u,v):
            mst.append((u,v,w))
            total_weight+=1
    return mst,total_weight

#prim's mst

def prim_mst(adj_list):
     
    all_nodes = set(adj_list.keys()) #adding all the nodes to a set
    for i in adj_list.values():
        for u,w in i:
            all_nodes.add(u)
    
    visited = set()
    source = 0
    visited.add(source)
    
    mst = []
    total_weight = 0
    
    edges = []
    for u in adj_list:
        for v,w in adj_list[u]:
            edges.append([w,u,v])
    while len(visited) < len(all_nodes):
        min_edge = None
        min_weight = float('inf')
        for u in visited:
            for v, w in adj_list.get(u, []):
                if v not in visited and w < min_weight:
                    min_edge = (u, v, w)
                    min_weight = w
        
        if min_edge is None:
            break
        visited.add(v)
        mst.append((u,v,w))
        total_weight += w
        
        for to, weight in adj_list.get(v, []):
            if to not in visited:
                edges.append((v, to, weight))
        
        for u,v,w in mst:
            print(f"{u} -> {v} (weight {w})")
        
        print("total weight : ",total_weight)
    
        
    

if __name__ == "__main__":
    print("dfs")
    dfs(adj_list)
    print("bfs")
    bfs(adj_list)
    print("dijakstra")
    dijkstra(adj_list)
    print("kruskal's mst")
    mst,weight = kruskal_mst(adj_list)
    for u,v,w in mst:
        print(f"{u} -> {v} (weight of {w})")
    print(f"total weight is : ",weight)
    print("mst")
    prim_mst(adj_list)