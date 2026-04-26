def containsCycle(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    
    def dfs(r, c, pr, pc, char):
        visited[r][c] = True
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] == char:
                    
                    if not visited[nr][nc]:
                        if dfs(nr, nc, r, c, char):
                            return True
                    
                    elif (nr, nc) != (pr, pc):
                        return True
        
        return False
    
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                if dfs(i, j, -1, -1, grid[i][j]):
                    return True
    
    return False

grid = [
    ["a","a","a","a"],
    ["a","b","b","a"],
    ["a","b","b","a"],
    ["a","a","a","a"]
]

print(containsCycle(grid)) 

grid = [
    ["c","c","c","a"],
    ["c","d","c","c"],
    ["c","c","e","c"],
    ["f","c","c","c"]
]

print(containsCycle(grid)) 

grid = [
    ["a","b","b"],
    ["b","z","b"],
    ["b","b","a"]
]

print(containsCycle(grid)) 



