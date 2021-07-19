"""
前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
请你实现 Trie 类：
    Trie() 初始化前缀树对象。
    void insert(String word) 向前缀树中插入字符串 word 。
    boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
    boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
例如：
    输入
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    输出
        [null, null, true, false, true, null, true]
    解释
        Trie trie = new Trie();
        trie.insert("apple");
        trie.search("apple");   // 返回 True
        trie.search("app");     // 返回 False
        trie.startsWith("app"); // 返回 True
        trie.insert("app");
        trie.search("app");     // 返回 True
"""
class TrieNode:
    def __init__(self) -> None:
        self.path = 0
        self.end = 0
        self.trieMap = dict()

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    # 插入方法的实现
    def insert(self, word):
        parent = self.root
        # parent表示每个树的点；每个点都有一个map结构存储下一个点
        for i in word:
            if i not in parent.trieMap:
                parent.trieMap[i] = TrieNode()
            # 赋值继续向下遍历
            parent = parent.trieMap[i]
            # 代表以点结尾作为前缀的路径 +1
            parent.path += 1
        # 最后结尾的点 end+1
        parent.end += 1
    
    # 检查一个完整的单词是否存在
    def search(self, word):
        parent = self.root
        for i in word:
            if i not in parent.trieMap:
                return False
            parent = parent.trieMap[i]
        # 遍历到最后一点 若end=0 则不是结尾点 只是一个前缀
        if parent.end > 0:
            return True
        return False

    # 检查前缀prefix是否存在
    def startsWith(self, prefix):
        parent = self.root
        for i in prefix:
            if i not in parent.trieMap:
                return False
            parent = parent.trieMap[i]
        if parent.path > 0:
            return True
        return False