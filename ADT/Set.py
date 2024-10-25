class _SetIterator:
    def __init__(self, elements):
        self._elements = elements
        self._index = 0

    def __next__(self):
        if self._index < len(self._elements):
            result = self._elements[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration


class set:
    # creates an array
    def __init__(self):
        self._elements = list()

    def __len__(self):
        return len(self._elements)

    def __contains__(self, X):
        return self._elements.__contains__(X)

    def add(self, x):
        if self.__contains__(x) == False:
            self._elements.append(x)

    def remove(self, x):
        if self.__contains__(x) == True:
            self._elements.remove(x)

    def __eq__(self, x):
        if len(self) == len(x):
            return self.ifSubSetof(x)
        return False

    def ifSubSetof(self, X):
        for x in X._elements:
            if x not in self._elements:
                return False
        return True

    def union(self, X):
        newSet = list(X._elements)
        newSet.extend(self.difference(X))
        return newSet

    def intersect(self, X):
        newSet = set()
        for x in self._elements:
            if x in X._elements:
                newSet.add(x)
        return newSet

    def difference(self, X):
        newSet = self._elements
        for x in X._elements:
            if x in newSet:
                newSet.remove(x)
        return newSet

    def __iter__(self):
        return _SetIterator(self._elements)


A = set()
B = set()

for i in range(5):
    A.add(i)
for i in range(3, 8):
    B.add(i)

# print(A._elements)
# print(B._elements)
# print(len(A))
# print(100 in A)
# print(3 in A)
# print(len(B))
# print(100 in B)
# print(2 in B)
# print(len(A)+len(B))
# A.remove(0)
# B.remove(3)
# C = A.intersect(B)
D = B.union(A)
print(D)
# print(D)
# print(D)
for i in D :
    print(i)
