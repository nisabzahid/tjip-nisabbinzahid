# T.C = insert O(N), search O(N), startsWith O(N) where N is the length of the word
# S.C = O(K) where k is sum of the length of the word
 
class TrieNode:
    def __init__(self):
        self.children = dict()
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

    def _find_node(self, word:str) -> TrieNode:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return None
            cur = cur.children[ch]
        return cur

    def search(self, word: str) -> bool:
        cur  = self._find_node(word)
        return cur is not None and cur.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)