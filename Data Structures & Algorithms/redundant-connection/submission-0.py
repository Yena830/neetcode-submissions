class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a]+=1
            indegree[b]+=1
        queue = deque()
        for key,val in indegree.items():
            if val==1:
                queue.append(key)
        while queue:
            node = queue.popleft()
            indegree[node]-=1
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==1:
                    queue.append(nei)
        for a,b in edges[::-1]:
            if indegree[a]>0 and indegree[b]>0:
                return [a,b]
        return [-1,-1]

