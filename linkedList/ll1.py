class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class LinkList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def add(self, data):
        temp = Node(data, self.head)
        self.head = temp
        self.size += 1

    def print_list(self):
        temp = self.head

        while temp:
            print temp.get_data(),
            temp = temp.get_next()

        print "\n"

    def insert_at_end(self, data):
        temp = Node(data)
        temp_i = self.head

        if not self.head:
            self.head = temp
            return

        while temp_i.get_next():
            temp_i = temp_i.get_next()

        temp_i.set_next(temp)

        self.size += 1

    def get_length(self):
        return self.size

    # pos start from index 0
    def insert_at_pos(self, pos, data):
        temp = Node(data)
        length = self.size
        if pos < 0 or pos > length:
            print "index out of range "
            return

        if pos == 0:
            self.size += 1
            temp.set_next(self.head)
            self.head = temp
            return
        temp_i = self.head
        prev = Node
        while pos and temp_i:
            pos -= 1
            prev = temp_i
            temp_i = temp_i.get_next()

        temp.set_next(temp_i)
        prev.set_next(temp)

    # pos start from index 0
    def delete_at_pos(self, pos):

        if pos < 0 or pos+1 > self.size:
            print "index out of range"
            return
        if self.size == 0:
            print "list already empty"
            return
        if pos == 0:
            temp = self.head
            nextNone = temp.get_next()
            del temp
            self.head = nextNone
            return
        prev = None
        temp = self.head

        while pos and temp:
            pos -= 1
            prev = temp
            temp = temp.get_next()

        prev.set_next(temp.get_next())
        del temp
        self.size -= 1

    def delete_with_key(self, key):
        prev = None
        temp = self.head
        while temp and temp.get_data() != key:
            prev = temp
            temp = temp.get_next()

        if not temp:
            print "key not found"
            return
        if not prev:
            # found at  start of list
            self.head = temp.get_next()
            del temp
            self.size -= 1
            return
        prev.set_next(temp.get_next())
        del temp
        self.size -= 1

    def find_length(self, temp):
        if not temp:
            return 0
        if not temp.get_next():
            return 1
        return 1 + self.find_length(temp.get_next())

    def search(self, key):
        temp = self.head
        while temp:
            if temp.get_data() == key:
                return True
            temp = temp.get_next()
        return False

    def search_recursive(self, key, temp):
        if not temp:
            return False
        if temp.get_data() == key:
            return True
        return self.search_recursive(key, temp.get_next())

    def swap_nodes(self, key1, key2):
        node1 = self.head
        prev1 = None
        while node1 and node1.get_data() != key1:
            prev1 = node1
            node1 = node1.get_next()

        node2 = self.head
        prev2 = None
        while node2 and node2.get_data() != key2:
            prev2 = node2
            node2 = node2.get_next()

        if not node1 or not node2:
            print "invalid keys"
            return
        if not prev2:
            # swap node1, node2 and prev1, prev2
            t = node1
            node1 = node2
            node2 = t
            t = prev1
            prev1 = prev2
            prev2 = t

        print node1.get_data()
        print node2.get_data()
        print prev2.get_data()
        if not prev1:
            # first node is head
            prev2.set_next(node1)
            tempNext = node1.get_next()
            node1.set_next(node2.get_next())
            node2.set_next(tempNext)
            self.head = node2
            return
        prev2.set_next(node1)
        tempNext = node1.get_next()
        node1.set_next(node2.get_next())
        prev1.set_next(node2)
        node2.set_next(tempNext)
        # self.head = node2

ll = LinkList()

ll.insert_at_pos(0, 4)

ll.print_list()
ll.add(1)
ll.add(2)
ll.add(3)
ll.print_list()
print ll.get_length()

ll.insert_at_end(0)
ll.insert_at_end(-1)

ll.print_list()

print ll.get_length()

ll.insert_at_pos(0, 4)

ll.print_list()

ll.insert_at_pos(8, -2)

ll.print_list()
ll.insert_at_pos(2, 5)
ll.print_list()

ll.delete_at_pos(0)
ll.print_list()

ll.delete_at_pos(6)
ll.print_list()

# ll.delete_at_pos(2)
# ll.print_list()
#
# ll.delete_with_key(3)
# ll.print_list()

# ll.delete_with_key(0)
# ll.print_list()
#
# ll.delete_with_key(1)
# ll.print_list()

print ll.find_length(ll.head)
ll.print_list()
#
# print ll.search_recursive(0, ll.head)
# print ll.search_recursive(5, ll.head)
# print ll.search_recursive(1, ll.head)
# print ll.search_recursive(-1, ll.head)

ll.swap_nodes(0,5)
ll.print_list()