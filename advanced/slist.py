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


s = SList()
s.insert_front("A")
s.insert_front("B")

i = s.search("A")

s.insert_after("C", i)

s.print_list()
