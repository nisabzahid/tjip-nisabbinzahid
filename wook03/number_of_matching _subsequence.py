# T.C = O(w * m), w is the number of words m is average 
# word length
# S.C = O(n * c) n is the length of s and c is the average number of children per Trie node.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = 0  

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word += 1

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def traverse(node, index):
            count = node.is_end_of_word 
            node.is_end_of_word = 0
            for char, child in node.children.items():
                next_index = s.find(char, index)  
                if next_index != -1:  
                    count += traverse(child, next_index + 1)
            return count
        trie = Trie()
        for word in words:
            trie.insert(word)
        return traverse(trie.root, 0)
