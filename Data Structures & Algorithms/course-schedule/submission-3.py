class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for pre,curr in prerequisites:
            graph[pre].append(curr)
            indegree[curr]+=1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)

        count = 0
        while queue:
            node = queue.popleft()
            count +=1
            for c in graph[node]:
                indegree[c]-=1
                if indegree[c]==0:
                    queue.append(c)
        return count == numCourses
        

