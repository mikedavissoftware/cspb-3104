import heapq

def prim(edge_list):
    # Build adjacency list
    adj = {}
    nodes = set()
    
    for u, v, w in edge_list:
        nodes.add(u)
        nodes.add(v)
        adj.setdefault(u, []).append((v, w))
        adj.setdefault(v, []).append((u, w))
    
    # Start from the smallest node for consistency
    start = min(nodes)
    
    visited = set([start])
    edges_heap = []
    
    # Push edges from the start node
    for v, w in adj[start]:
        heapq.heappush(edges_heap, (w, start, v))
    
    mst = []
    
    while edges_heap and len(visited) < len(nodes):
        w, u, v = heapq.heappop(edges_heap)
        
        if v in visited:
            continue
        
        visited.add(v)
        mst.append((u, v, w))
        
        for next_v, next_w in adj[v]:
            if next_v not in visited:
                heapq.heappush(edges_heap, (next_w, v, next_v))
    
    # Ensure edges are (i, j, w) with i < j
    mst = [(min(u, v), max(u, v), w) for u, v, w in mst]
    
    # Sort final MST in natural order
    mst.sort(key=lambda x: (x[0], x[1], x[2]))
    
    return mst