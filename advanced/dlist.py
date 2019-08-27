class DList:

    class Node:
        def __init__(self, item, front, back):
            self.item = item
            self.front = front
            self.back = back

    def __init__(self):
        self.size = 0
        self.head = self.Node(None, None, None)
        self.rear = self.Node(None, self.head, None)
        self.head.back = self.rear

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, item):
        a = self.Node(item, None, self.head)
        self.head.back.head = a
        self.head = a

    def insert_before(self, item, p):
        a = self.Node(item, p.front, p)
        p.front = a
        a.front.back = a

        self.size += 1

    def insert_after(self, item, p):
        t = p.back
        a = self.Node(item, p, t)
        p.front = a
        t.front = a

        self.size += 1

    def delete_front(self):
        self.head = self.head.back
        self.head.front = None

    def delete_back(self):
        self.rear.front.back = None
        self.rear = self.rear.front


    def print_list(self):
        p = self.head

        while p.item != None:
            print(p.item)
            p = p.back


d = DList()
d.insert_front("A")
d.insert_front("B")
d.insert_front("C")
d.insert_front("D")
d.insert_front("E")
d.print_list()
print()
d.delete_front()
d.delete_back()
d.print_list()

a = [2,4,5,7]

print(a[1-2])