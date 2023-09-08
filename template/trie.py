class Trie:
    def __init__(self, words=[]):
        self.root = {"length": 0}
        for word in words:
            self.insert(word)
            
    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {"length": 0}
            current["length"] += 1
            current = current[c]
        current["length"] += 1
        current["?"] = True

    def remove(self, word):
        current = self.root
        current["length"] -= 1
        for i, c in enumerate(word):
            if c in current:
                current[c]["length"] -= 1
                if current[c]["length"] < 1:
                    del current[c]
                    break
                else:
                    current = current[c]
        if i == len(word) - 1 and "?" in current:
            current.pop("?")

    # return 2 if exist or 1 if prefix, 0 if not found
    def contains(self, word):
        current = self.root
        for c in word:
            if c not in current:
                return 0
            current = current[c]
        return 2 if "?" in current else 1