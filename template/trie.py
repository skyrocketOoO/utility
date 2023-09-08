class Trie:
    def __init__(self, words=[]):
        self.root = {"length": 0}
        for word in words:
            self.insert(word)
            
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {"length": 0}
            cur["length"] += 1
            cur = cur[c]
        cur["length"] += 1
        cur["end"] = True

    def remove(self, word):
        cur = self.root
        cur["length"] -= 1
        for i, c in enumerate(word):
            if c in cur:
                cur[c]["length"] -= 1
                if cur[c]["length"] < 1:
                    del cur[c]
                    break
                else:
                    cur = cur[c]
        if i == len(word) - 1 and "end" in cur:
            del cur["end"]

    # 2 represent containes, 1 represent prefix, 0 represent False
    def contains(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                return 0
            cur = cur[c]
        return 2 if "end" in cur else 1