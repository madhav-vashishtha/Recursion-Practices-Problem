from functools import lru_cache

def get_pos(c):
    x = ord(c) - ord('A')
    return (x // 6, x % 6)

def dist(a, b):
    if a is None or b is None:
        return 0
    x1, y1 = get_pos(a)
    x2, y2 = get_pos(b)
    return abs(x1 - x2) + abs(y1 - y2)

def minimumDistance(word):

    @lru_cache(None)
    def dp(i, f1, f2):
        if i == len(word):
            return 0
        
        curr = word[i]
        
        use_f1 = dist(f1, curr) + dp(i + 1, curr, f2)
        
        use_f2 = dist(f2, curr) + dp(i + 1, f1, curr)
        
        return min(use_f1, use_f2)
    
    return dp(0, None, None)


print(minimumDistance("CAKE"))   
print(minimumDistance("HAPPY"))  
