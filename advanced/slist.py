class SList:

    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def insert_after(self, item, p):
        p.next = self.Node(item, p.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty(): print("error")
        else:
            
            self.head = self.head.next

            size -= 1

    def delete_after(self, p):
        t=p.next
        p.next = t.next
        self.size -= 1

    def search(self, t):
        h = self.head

        for i in range(self.size):
            if t == h.item: return h
            h = h.next

        return None

    def print_list(self):
        h = self.head

        while h != None:
            print(h.item)

            h = h.next

    def merge(self, l2):

        h1 = self.head
        h2 = l2.head

        if h1.item > h2.item:
            self.insert_front(h2.item)
            h2 = h2.next
            h1 = self.head

        while h2 and h1.next:
            if h1.next.item > h2.item:
                self.insert_after(h2.item, h1)
                h2 = h2.next

            else:
                h1=h1.next

        while h2:
            self.insert_after(h2.item, h1)
            h2 = h2.next
            h1 = h1.next






s1 = SList()
s1.insert_front(40)
s1.insert_front(7)
s1.insert_front(3)

s2 = SList()
s2.insert_front(4)
s2.insert_front(2)


s1.merge(s2)

s1.print_list()
