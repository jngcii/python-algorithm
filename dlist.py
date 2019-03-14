class DList:

    class Node:

        def __init__(self, item, prev, next):

            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self, item):

        self.head = self.Node(item, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 1


    def is_empty(self): return self.size == 0
    def size(self): return self.size


    def insert_front(self, item, p):

        t = p.prev
        new_node = self.Node(item, t, p)
        p.prev = new_node
        t.next = new_node
        self.size += 1


    def insert_after(self, p, item):

        t = p.next
        new_node = self.Node(item, p, t)
        p.next = new_node
        t.prev = new_node
        self.size += 1


    def delete(self, item):

        p = item.prev
        t = item.next

        p.next = t
        t.prev = p

        self.size -= 1


    def search(self, target):

        p = self.head

        for k in range(0, self.size):

            if p.item == target:

                return p

            p = p.next

        print("None")
        return


    def print_list(self):

        p = self.head

        while p:

            if p.next:
                print(p.item, " -> ", end='')

            else:
                print(p.item)

            p = p.next
