# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for crs,prq in prerequisites:
            graph[crs].append(prq)
        
        state = [0]*numCourses
        topological_sorted = []

        def dfs(course):
            if state[course] == 2:
                return True
                
            if state[course] == 1 :
                return False
            
            state[course] = 1
            for neighbor in graph[course]:
                if  not dfs(neighbor):
                    return False
            
            topological_sorted.append(course)
            state[course] = 2

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        

            

