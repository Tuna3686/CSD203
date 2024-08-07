from DoubleLinkList import * 
'''
mylist = DBLinkList()

mylist.addFirst("A",20)
mylist.addFirst("B",21)
mylist.addFirst("C",22)
mylist.addLast("X",19)
mylist.addLast("Y",18)
mylist.addLast("Z",17)
mylist.addIndex("Aa",25,3)
mylist.display()
mylist.addIndex("qq",25,4)
mylist.display()

'''

        
mylist = DBLinkList()

mylist.addFirst("A",20)
mylist.addFirst("B",21)
mylist.addFirst("C",22)
mylist.addLast("X",19)
mylist.addLast("Y",18)
mylist.addLast("Z",17)
mylist.delIndex(3)


mylist.addIndex("qq",25,4)

mylist.reverse()
mylist.display()


