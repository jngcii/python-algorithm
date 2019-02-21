class SList:

    class Node:

        def __init__(self, item, next):

            self.item = item
            self.next = next

    def __init__(self):

        self.head = None
        self.size = 0


    def is_empty(self): return self.size == 0
    def size(self): return self.size


    def push(self, item):

        if self.is_empty():
            new_node = self.Node(item, None)
            self.head = new_node

        else:
            new_node = self.Node(item, self.head)
            self.head = new_node
        self.size += 1


    def insert_after(self, item, p):

        new_node = self.Node(item, p.next)
        p.next = new_node
        self.size += 1


    def pop(self):

        if self.is_empty():
            print("there is no item to delete.")
            return

        else:
            h = self.head
            self.head = h.next
            self.size -= 1
            return h.item


    def delete_after(self, p):

        if self.is_empty():
            print("there is no item to delete.")

        else:
            p.next = p.next.next
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
