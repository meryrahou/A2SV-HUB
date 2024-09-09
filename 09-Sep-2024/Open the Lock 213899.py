# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        state = '0000'
        if state in deadends:
            return -1
        
        queue = deque([state])
        visited = set([state])

        def getNeighbors(state):
            neighbors = []
            for i in range(4):
                for d in [-1, 1]: 
                    new_digit = (int(state[i]) + d) % 10
                    neighbor = state[:i] + str(new_digit) + state[i+1:]  
                    neighbors.append(neighbor)  
            return neighbors

        cpt = 0
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target:
                    return cpt

                neighbors = getNeighbors(current)
                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in deadends:
                        visited.add(neighbor)
                        queue.append(neighbor)

            cpt += 1

        return -1 