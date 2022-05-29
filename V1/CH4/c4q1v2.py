from collections import deque

def hasRoute(graph, S, E):
    """
    check if route exists in directed graph between nodes S and E
    """
    if S == E:
        return True
    seen = {}
    queue = deque()
    queue.append(S)
    while queue:
        curr = queue.popleft()
        for edge in graph[curr]:
            if edge == E: # or edge is E if they're the same object
                return True
            if edge not in seen:
                queue.append(edge)
                seen[edge] = curr 
    return False
    
            
    
