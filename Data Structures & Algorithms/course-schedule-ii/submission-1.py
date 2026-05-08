class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))
        res = []
        indegree = [0]*numCourses
        graph = defaultdict(list)
        for curr,pre in prerequisites:
            graph[pre].append(curr)
            indegree[curr]+=1
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for c in graph[curr]:
                indegree[c]-=1
                if indegree[c]==0:
                    queue.append(c)
        return res if len(res)==numCourses else []