class _MapIterator:
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


class _MapEntry:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class Map:
    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    def add(self, key, value):
        index = self._findPosition(key)
        if index is not None:
            self._entryList[index].value = value
            return False
        entry = _MapEntry(key, value)
        self._entryList.append(entry)
        return True

    def valueOf(self, key):
        ndx = self._findPosition(key)
        if ndx == None:
            return ndx
        return self._entryList[ndx].value

    def remove(self, key):
        ndx = self._findPosition(key)
        assert ndx != None, "Invalid key"
        self._entryList.pop(ndx)

    def __iter__(self):
        return _MapIterator(self._entryList)

    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None


M = Map()

M.add(100, "TNT")
M.add(101, "Tanim")
M.add(100, "Fahim")
for i in M:
    print(i.key, " ", i.value)
print(M[100])
print()
