def find_cyclic_vertices(self, graph: List[List[int]]) -> List[int]:
    # using dfs
    def dfs(u, status):
        # init to unsafe
        status[u] = 2

        for v in graph[u]:
            if status[v] == 0: # not visited
                if dfs(v, status):
                    return True
            elif status[v] == 2: # if u has edge to unsafe v, u also unsafe
                return True
        
        # if all check passed, u is safe
        status[u] = 1
        return False

    n = len(graph)
    # 0: not visited, 1: status, 2: unsafe
    status = [0] * n 
    for u in range(n):
        if status[u] == 0:
            dfs(u, status)
            
    return [u for u in range(n) if status[u] == 1]
