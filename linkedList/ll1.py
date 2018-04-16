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

ll.delete_at_pos(2)
ll.print_list()

ll.delete_with_key(3)
ll.print_list()

# ll.delete_with_key(0)
# ll.print_list()
#
# ll.delete_with_key(1)
# ll.print_list()

print ll.find_length(ll.head)
ll.print_list()

print ll.search(0)
# print ll.search(5)
# print ll.search(1)
# print ll.search(-1)