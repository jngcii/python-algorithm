from slist import SList

def reverse(s, h):

    if h.next is None:

        s.head = h

    else:

        reverse(s, h.next)

        h.next.next = h


def reverse_slist(s):

    h = s.head

    reverse(s, s.head)

    h.next = None


s = SList()
s.insert_front(11)
s.insert_front(9)
s.insert_front(7)
s.insert_front(5)
s.insert_front(4)
s.insert_front(2)
s.print_list()

reverse_slist(s)
s.print_list()
