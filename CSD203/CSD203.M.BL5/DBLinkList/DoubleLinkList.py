from Student import *
from Node import *

class DBLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    #end def
    
    def isEmpty(self):
        return self.head == None or self.tail == None or self.size == 0
    
    def addFirst(self,name,age):
        node = Node(Student(name,age))
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node
        self.size += 1
        
    def addLast(self,name,age):
        node = Node(Student(name,age))
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.pre = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
        
    def reverse(self): #display from tail to head
        if self.isEmpty(): return
        cur = self.tail
        while cur:
            print(f"{cur.data}," ,end= " ")
            cur = cur.pre
        print()
        
    def display(self):
        if (self.isEmpty()): return
        cur = self.head
        while cur:
            print(f"{cur.data}", end=" ")
            cur = cur.next
        print()
        
    def delFirst(self):
        if self.isEmpty(): return None
        if self.size == 1:
            temp = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return temp
        temp = self.head.data
        self.head.next.pre = None
        self.head = self.head.next
        self.size -= 1
        return temp
    
    def delLast(self):
        if self.isEmpty(): return None
        if self.size == 1:
            temp = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return temp
        temp = self.tail.data
        self.tail.pre.next = None
        self.tail = self.tail.pre
        self.size -= 1
        return temp

    def addIndex(self, name, age, index):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addFirst(name, age)
            return
        if index == self.size:
            self.addLast(name, age)
            return

        cur = self.head
        for _ in range(index):
            cur = cur.next

        new_node = Node(Student(name, age))
        new_node.next = cur
        new_node.pre = cur.pre
        if cur.pre is not None:
            cur.pre.next = new_node
        cur.pre = new_node

        self.size += 1

    def delIndex(self, index):
        if index < 0:
            return
        if index == 0:
            return self.delFirst()
        count = 0
        cur = self.head
        while cur:
            if index == count + 1:
                break
            count += 1
            cur = cur.next
        if cur is None or cur.next is None:
            return
        elif cur.next.next is None:
            return self.delLast()
        else:
            temp = cur.next.data
            cur.next = cur.next.next
            cur.next.pre = cur
            self.size -= 1
            return temp

