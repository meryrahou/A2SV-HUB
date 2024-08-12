# Problem: D - Conveyor Belts - https://codeforces.com/gym/500425/problem/D

testcases = int(input())

for _ in range(testcases):
    n, x1, y1, x2, y2 = map(int, input().split())

    layer1 = min(min(x1, n-x1+1), min(y1, n-y1+1))
    layer2 = min(min(x2, n-x2+1), min(y2, n-y2+1))
    
    # If both points are in the same layer
    if layer1 == layer2:
        print(0)
    else:
        # Calculate energy needed
        energy = abs(layer1 - layer2)
        print(energy)
 