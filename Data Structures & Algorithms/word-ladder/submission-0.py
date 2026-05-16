class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        input:
            beginWord
            endWord
            wordList -> the words that can be used

        """
        if beginWord == endWord:
            return 1
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        n = len(beginWord)
        similar = defaultdict(list)
        for word in wordList:
            for i in range(n):
                curr = word[:i]+"*"+word[i+1:]
                similar[curr].append(word)
        queue = deque([(beginWord,1)])
        visited = set()
        while queue:
            word,step = queue.popleft()
            visited.add(word)
            for i in range(n):
                curr = word[:i]+"*"+word[i+1:]
                for nei in similar[curr]:
                    if nei == endWord:
                        return step+1
                    if nei not in visited:
                        queue.append((nei,step+1))
        return 0

        


