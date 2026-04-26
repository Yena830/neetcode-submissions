"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}
        def dfs(curr):
            if curr in node_map:
                return node_map[curr]
            node_map[curr] = Node(curr.val)
            for nei in curr.neighbors:
                node_map[curr].neighbors.append(dfs(nei))
            return node_map[curr]
        if not node:
            return None
        dfs(node) 
        return node_map[node]