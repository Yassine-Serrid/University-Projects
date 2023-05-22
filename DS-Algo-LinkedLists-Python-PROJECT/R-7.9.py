'''
HW5
Q NUMBER# R-7.9
Yessin nader serrid
2181156439
'''

class DNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def setPrev(self,newPrev):
        self.prev = newPrev

class ConcatDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.trail = None


    def insertInDList(self, key):
        temp = DNode(key)
        if self.head == None:
            temp.setNext(self.head)
            temp.setPrev = None
            self.head = temp
        else:
            curr = self.head
            while curr.getNext() != None:
                    curr = curr.getNext()
            curr.setNext(temp)
            temp.setPrev(curr)
            temp.setNext(None)
            self.trail = temp


    def displayList(self):
        temp = self.head
        while temp != None:
            print(temp.getData(), end=" ")
            temp = temp.getNext()
        print()


    def concatList(self, list2):
        if self.trail != None and list2.head != None:
            self.trail.setNext(list2.head)


if __name__ == "__main__":
    dlist1 = ConcatDoublyLinkedList()

    dlist1.insertInDList(4)
    dlist1.insertInDList(14)
    dlist1.insertInDList(3)
    dlist1.insertInDList(98)



    print("Initial list 1: ")
    dlist1.displayList()

    dlist2 = ConcatDoublyLinkedList()
    dlist2.insertInDList(16)
    dlist2.insertInDList(13)
    dlist2.insertInDList(44)


    print("Initial list 2: ")
    dlist2.displayList()

    print("After concatenating list1 with list2: ")
    dlist1.concatList(dlist2)
    dlist1.displayList()


"""
OUTPUT:
Initial list 1: 
4 14 3 98 
Initial list 2: 
16 13 44 
After concatenating list1 with list2: 
4 14 3 98 16 13 44 
"""
