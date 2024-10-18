# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())  
for _ in range(t):
    m = int(input())  
    p = list(map(int, input().split()))  
    
    def make_beautiful(l, r):
        # Base case
        if l == r:
            return 0, [p[l]]  
        
        # Recursively process the left and right
        mid = (l + r) // 2
        left_ops, left_half = make_beautiful(l, mid)
        right_ops, right_half = make_beautiful(mid + 1, r)
        
        if left_ops == -1 or right_ops == -1:
            return -1, []
        
        # We now have two halves, check if we need to swap
        if left_half[-1] < right_half[0]:
            # Already sorted, no need to swap
            return left_ops + right_ops, left_half + right_half
        elif right_half[-1] < left_half[0]:
            # Swap needed
            return left_ops + right_ops + 1, right_half + left_half
        else:
            return -1, []
    
    min_ops, sorted_p = make_beautiful(0, m - 1)
    print(min_ops)

