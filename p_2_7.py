from slist import SList

def merge_slist(s1, s2):

    h2 = s2.head


    for k in range(s2.size):

        h1 = s1.head
        n1 = h1.next

        if h2.next != None:

            for j in range(s1.size):

                if h1.next != None:

                    if h2.item < h1.item:

                        s1.insert_front(h2.item)

                    elif h2.item > h1.item and h2.item < n1.item:

                        s1.insert_after(h2.item, h1)

                    h1 = h1.next
                    if n1.next != None:
                        n1 = n1.next

            h2 = h2.next


s1 = SList()
s1.insert_front(11)
s1.insert_front(9)
s1.insert_front(7)
s1.insert_front(5)
s1.insert_front(4)
s1.insert_front(2)

s2 = SList()
s2.insert_front(8)
s2.insert_front(6)
s2.insert_front(3)
s2.insert_front(1)

merge_slist(s1, s2)

s1.print_list()
