from typing import List

# T.C = O(M×N×4L), where 𝑀,𝑁 are board dimensions and 
#L is the maximum word length.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_word = True
    
    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.is_word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ROWS, COLS = len(board), len(board[0])
        result = set()
        visited = set()
        
        def dfs(r, c, node, path):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            path += board[r][c]
            
            if node.is_word:
                result.add(path)
            
            # Explore neighbors
            dfs(r+1, c, node, path)
            dfs(r-1, c, node, path)
            dfs(r, c+1, node, path)
            dfs(r, c-1, node, path)
            
            # Backtrack
            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")
        
        return list(result)
