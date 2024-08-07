from Node import*
from Student import*
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    #end def
    def isEmpty(self):
        return self.head == None
    
    def push(self,name,age):
        if(name[0]=="X"):
            return
        node = Node(Student(name,age))
        if (self.isEmpty()):
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size +=1
    #end def
        
    def display(self):
        if (self.isEmpty()): return
        cur = self.head
        while cur:
            print(f"{cur.data}", end=" ")
            cur = cur.next
        print()
    
    def top(self):
        if self.isEmpty(): return None
        return self.head.data
    
    def pop(self):
        if self.isEmpty():
            return None
        temp = self.head.data
        self.head = self. head.next
        self.size -=1
        return temp



    def findIndex(self,k):
        count = 0
        cur = self.head
        index = 0
        post = 0
        while cur:
            if count == k:
                return index
            index += 1
            if self.check(cur.data.Age):
                count += 1
                post = index
            cur = cur.next
        if k == -1:
            return post
        else:
            return -1
    
    def sort(self):
        if self.isEmpty() or self.head == self.tail : return
        i = self.head
        while i.next :
            j = i.next
            while j:
                if i.data.Age > j.data.Age :
                    temp = i.data
                    i.data = j.data
                    j.data = temp
                j = j.next
            i = i.next

    def sortEven(self):
        if self.isEmpty() or self.head == self.tail : return
        i = self.head
        while i.next :
            j = i.next
            while j:
                x1 = i.data.Age
                x2 = j.data.Age
                change = False
                if self.is_even(x1) and self.is_even(x2) :
                    if x1>x2:
                        change = True
                    elif x1 == x2:
                        if i.data.Name < j.data.Name:
                            change = True
                    if change:
                        temp = i.data
                        i.data = j.data
                        j.data = temp
                j = j.next
            i = i.next