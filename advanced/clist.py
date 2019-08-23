class CList:

    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def get_size(self):
        return self.size

    def insert(self, item):
        a = self.Node(item,None)

        if self.size == 0:
            a.next = a
            self.last = a
        else:
            a.next = self.last.next
            self.last.next = a

        self.size +=1

    def first(self):
        return self.last.next.item

    def delete(self):
        p = self.last.next

        if self.size == 1:
            self.last = None
        else:
            self.last.next = p.next
        
        self.size -= 1

    def print_list(self):
        f = self.last.next
        p = f
        while p.next != f:
            print(p.item)
            p=p.next
        print(p.item)




c = CList()
c.insert("A")
c.insert("B")
c.insert("C")
c.delete()
c.print_list()