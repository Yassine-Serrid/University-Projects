'''
HW5
Q NUMBER# R-7.2
Yessin nader serrid
2181156439
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SLL:

    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is not None:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data, None)
        else:
            self.head = Node(data, None)

    def printList(self):
        if self.head is not None:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
        else:
            print("List is empty")


def concatLL(firstLinkedList, secondLinkedList):
    newList = SLL()
    temp = firstLinkedList.head
    while temp is not None:
        newList.add(temp.data)
        temp = temp.next

    temp = secondLinkedList.head
    while temp is not None:
        newList.add(temp.data)
        temp = temp.next

    return newList


print("Initial list 1: ")
firstLinkedList = SLL()

firstLinkedList.add(4)
firstLinkedList.add(14)
firstLinkedList.add(3)
firstLinkedList.add(98)
firstLinkedList.printList()

print("\nInitial list 2: ")

secondLinkedList = SLL()

secondLinkedList.add(16)
secondLinkedList.add(13)
secondLinkedList.add(44)


secondLinkedList.printList()

print("\nAfter concatenating list1 with list2: ")
concatenatedList = concatLL(firstLinkedList, secondLinkedList)
concatenatedList.printList()

"""
OUTPUT:
Initial list 1: 
4 14 3 98 
Initial list 2: 
16 13 44 
After concatenating list1 with list2: 
4 14 3 98 16 13 44 
"""