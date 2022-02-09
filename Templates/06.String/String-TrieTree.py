class Trie:
    
    # 初始化字典树
    def __init__(self):
        self.children = dict()
        self.isEnd = False

    # 向字典树中插入一个单词
    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True

    # 查找字典树中是否存在一个单词
    def search(self, word: str) -> bool:
        cur = self
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return cur is not None and cur.isEnd

    # 查找字典树中是否存在一个前缀
    def startsWith(self, prefix: str) -> bool:
        cur = self
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur is not None