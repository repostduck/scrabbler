from collections.abc import MutableMapping
class ReversibleList(MutableMapping):
    def __init__ (self, data = []):
        self.__data__ = list(data)
        self.__len__ = len(data)
    def __getitem__ (self, index):
        return self.__data__[index]
    def __setitem__ (self, index, value):
        self.__data__[index] = value
        self.__len__ += 1
    def __delitem__ (self, index):
        del self.__data__[index]
        self.__len__ -= 1
    def __iter__ (self):
        return iter(self.__data__)
    def __len__ (self):
        return self.__len__
    def append (self, value):
        self.__data__.append(value)
        self.__len__ += 1
    def reverse (self):
        rev = ReversibleList()
        for i in range(len(self) - 1, -1, -1):
            rev.append(self.get(i))
        return rev
    def copy (self):
        l2 = ReversibleList()
        for i in range(len(self)):
            l2.append(self.get(i))
        return l2
    def __str__ (self):
        return str(self.__data__)
    @classmethod 
    def unite (cls, l1, l2):
        l3 = l1.copy()
        for j in range(len(l2)):
            l3.append(l2.get(j))
        return l3

#LinkedList is a list of Nodes, and is not iterable
#last node links back to the first node

class Node:
        def __init__ (self, value, next):
            self.__value__ = value
            self.__next__ = None
        def __getitem__(self):
            return self.__value__
        def __setitem__(self, value):
            self.__value__ = value
        def set_next(self, next):
            self.__next__ = next
        def get_next(self):
            return self.__next__
class LinkedList:
    def __init__ (self, data):
        self.__data__ = []
        for i in range(len(data)):
            self.__data__.append(Node(data[i]))
        self.__head__ = self.__data__[0]
        for j in range(len(self.__data__) - 1):
            self.__data__[j].set_next(self.__data__[j + 1])
        self.__data__[len(self.__data__) - 1].set_next(self.__data__[0])
    
    def __getitem__ (self, key):
        return self.__data__[key]

    def __setitem__ (self, key, value):
        self.__data__[key].set(value)

        
