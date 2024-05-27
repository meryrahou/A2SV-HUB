# Problem: Tower of Hanoi - https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1

    if N == 0:
        return 0

    # Step count for recursive calls
    steps = 0

    # Move N-1 disks from from_rod to aux_rod using to_rod as auxiliary
    steps += toh(N-1, from_rod, aux_rod, to_rod)
    
    # Move the N-th disk from from_rod to to_rod
    print("move disk {} from rod {} to rod {}".format(N, from_rod, to_rod))
    steps += 1
    
    # Move N-1 disks from aux_rod to to_rod using from_rod as auxiliary
    steps += toh(N-1, aux_rod, to_rod, from_rod)

    return steps
