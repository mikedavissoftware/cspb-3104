def kruskal(edge_list):
    # Sort edges by weight, then by nodes for consistency
    edges = sorted(edge_list, key=lambda x: (x[2], x[0], x[1]))
    
    # Find all unique nodes
    nodes = set()
    for u, v, _ in edges:
        nodes.add(u)
        nodes.add(v)
    
    # Union-Find setup
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        
        if root_x == root_y:
            return False  # Cycle
        
        # Union by rank
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        
        return True
    
    mst = []
    
    for u, v, w in edges:
        if union(u, v):
            mst.append((u, v, w))
    
    # Ensure edges are (i, j, w) with i < j
    mst = [(min(u, v), max(u, v), w) for u, v, w in mst]
    
    # Sort final MST in natural order
    mst.sort(key=lambda x: (x[0], x[1], x[2]))
    
    return mst