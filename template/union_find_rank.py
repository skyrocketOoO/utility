class UnionFindWithRank:
    def __init__(self, elements):
        self.parents = {}  # Initialize a dictionary to store parents
        self.ranks = {}    # Initialize a dictionary to store ranks
        self.init_ranks(elements)

    # Initialize ranks for each element
    def init_ranks(self, elements):
        for ele in elements:
            self.ranks[ele] = 0

    # Given an element, find the root of the group to which this element belongs.
    def find(self, x):
        # This may be the first time we see x, so set itself as the root.
        if x not in self.parents:
            self.parents[x] = x
        # If x != parents[x], we use the find function again on x's parent parents[x]
        # until we find the root and set it as the parent (value) of x in parents.
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # Given two elements x and y, merge the groups to which they belong.
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        # Set the root with lower rank as the parent
        if self.ranks[rootX] < self.ranks[rootY]:
            self.parents[rootX] = rootY
        elif self.ranks[rootX] > self.ranks[rootY]:
            self.parents[rootY] = rootX
        else:
            # If ranks are equal, choose one as the parent and increment its rank
            self.parents[rootY] = rootX
            self.ranks[rootX] += 1

class UnionFindWithRank:
    def __init__(self):
        self.parents = {}  # Initialize a dictionary to store parents

    # Given an element, find the root of the group to which this element belongs.
    def find(self, x):
        # This may be the first time we see x, so set itself as the root.
        if x not in self.parents:
            self.parents[x] = x
        # If x != parents[x], we use the find function again on x's parent parents[x]
        # until we find the root and set it as the parent (value) of x in parents.
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # Given two elements x and y, merge the groups to which they belong.
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        # Set the root with lower rank as the parent
        if rootX < rootY:
            self.parents[rootY]

        if rootX > rootY:
            self.parents[rootX] = rootY
        elif rootX < rootY:
            self.parents[rootY] = rootX


if __name__ == "__main__":
    # Example usage:
    elements = [1, 2, 3, 4, 5]
    uf = UnionFindWithRank(elements)
    uf.union(1, 2)
    uf.union(2, 3)

    # Find the root of an element
    print(uf.find(1))  # Output: 3 (since 1, 2, and 3 are in the same group)
    print(uf.find(4))  # Output: 4 (since 4 is in its own group)
