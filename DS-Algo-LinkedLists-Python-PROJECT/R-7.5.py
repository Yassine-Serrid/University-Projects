'''
HW5
Q NUMBER# R-7.5
Yessin nader serrid
2181156439
'''

class CircularLinkedList:
    class _LinkedListNode:
        __slots__ = '_data', '_next'
        def __init__(self, data, _next=None):
            self._data = data
            self._next = _next

    def __init__(self):

        self._head = CircularLinkedList._LinkedListNode(None, None)
        self._head._next = self._head
    def add_nodes(self, data):


        if data is None or data == []:
            return
        for item in data:
            self._head._next = CircularLinkedList._LinkedListNode(item, self._head._next)
    def __len__(self):
        if self._head is None or self._head._next == self._head:
            return 0
        length = 0
        temp = self._head._next
        while temp != self._head:
            temp = temp._next
            length += 1
        return length
    def __str__(self):
        data = []
        temp = self._head._next
        while temp._next != self._head:
            data.append(str(temp._data))
            temp = temp._next
        data.append(str(temp._data))
        return "[ {} ]".format(", ".join(data))


if __name__ == '__main__':
    cll1 = CircularLinkedList()
    cll1.add_nodes([1])
    print("Number of Nodes = {}".format(len(cll1)))
    print(cll1)
    cll1.add_nodes([2, 3, 4])
    print("Number of Nodes = {}".format(len(cll1)))
    print(cll1)

"""
OUTPUT:
Number of Nodes = 1
[ 1 ]
Number of Nodes = 4
[ 4, 3, 2, 1 ] 
"""
