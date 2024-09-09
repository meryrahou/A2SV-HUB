# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        result = []

        def constructGraph(current, parent):
            if not current:
                return

            if parent:
                graph[current].append(parent)
                graph[parent].append(current)
            
            constructGraph(current.left, current)
            constructGraph(current.right, current)

        constructGraph(root, None)

        queue = deque([target])
        visited = set([target])
        distance = 0

        while queue:
            if distance == k:
                result = [node.val for node in queue]
                break
            
            for _ in range(len(queue)):
                current = queue.popleft()

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                    
            distance += 1
        
        return result

