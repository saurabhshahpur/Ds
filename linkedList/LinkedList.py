from Node import Node


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
            print "index out of range, index start from 0"
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
        self.size += 1

    # pos start from index 0
    def delete_at_pos(self, pos):

        if pos < 0 or pos + 1 > self.size:
            print "index out of range, index start from 0"
            return
        if self.size == 0:
            print "list already empty"
            return
        if pos == 0:
            temp = self.head
            nextNone = temp.get_next()
            del temp
            self.size -= 1
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

    # n start with index 0
    def get_nth_node(self, n):
        temp = self.head
        if n < 0 or self.size < n + 1:
            return "index out of range, index start from 0"

        while temp and n:
            temp = temp.get_next()
            n -= 1

        return temp.get_data()

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.get_next() and fast.get_next().get_next():
            fast = fast.get_next().get_next()
            slow = slow.get_next()
        if not slow:
            return "list empty"
        return slow.get_data()

    def delete_list(self):
        while self.head:
            temp = self.head
            self.head = self.head.get_next()
            self.size -= 1
            del temp
        return True

    # n is 1 base index
    def get_nth_node_from_end(self, n):
        # print self .size
        if n < 1 or n > self.size:
            return "index out of range index start from 1"
        slow = self.head
        fast = self.head
        n -= 1
        while n and fast:
            n -= 1
            fast = fast.get_next()
        while fast.get_next():
            fast = fast.get_next()
            slow = slow.get_next()
        return slow.get_data()

    def count_key(self, key):
        temp = self.head
        count = 0
        while temp:
            if temp.get_data() == key:
                count += 1
            temp = temp.get_next()
        return count

    def reverse(self, temp):
        if not temp or not temp.get_next():
            return temp
        tem_next = temp.get_next()
        rev = self.reverse(temp.get_next())
        temp.set_next()
        tem_next.set_next(temp)
        self.head = rev
        return rev

    def set_loop(self, key):
        # find end of list and sent its next to key1
        temp = self.head
        while temp and temp.get_data() != key:
            temp = temp.get_next()

        if not temp:
            print "key not found"
            return

        temp1 = self.head
        while temp1.get_next():
            temp1 = temp1.get_next()

        temp1.set_next(temp)
        return

    def check_loop(self):

        slow = self.head
        fast = self.head
        if not fast:
            return False
        fast = fast.get_next()

        while fast and fast.get_next() and fast.get_next().get_next():
            if fast == slow:
                return True
            fast = fast.get_next().get_next()
            slow = slow.get_next()
        if not fast or not fast.get_next() or not fast.get_next().get_next():
            return False

    def merge_list(self, list1):
        temp = self.head
        temp1 = list1
        flist = None
        while temp and temp1:
            if temp1.get_data() < temp.get_data():
                tnode = Node(temp1.get_data(), flist)
                flist = tnode
                temp1 = temp1.get_next()
            else:
                tnode = Node(temp.get_data(), flist)
                flist = tnode
                temp = temp.get_next()

        while temp:
            tnode = Node(temp.get_data(), flist)
            flist = tnode
            temp = temp.get_next()

        while temp1:
            tnode = Node(temp1.get_data(), flist)
            flist = tnode
            temp1 = temp1.get_next()
        self.head = flist
        self.reverse(self.head)

ll = LinkList()

# ll.insert_at_pos(0, 4)

# ll.print_list()
ll.add(1)
ll.add(3)
ll.add(5)
# ll.print_list()
# print ll.get_length()

ll.insert_at_end(-1)
ll.insert_at_end(-3)

# ll.print_list()

# print ll.get_length()

# ll.insert_at_pos(0, 4)

# ll.print_list()
# print ll.get_length()

# ll.insert_at_pos(8, -2)
#
# ll.print_list()
# print ll.get_length()

# ll.insert_at_pos(2, 5)
# ll.print_list()
# print ll.get_length()


# ll.delete_at_pos(0)
# ll.print_list()

# ll.delete_at_pos(6)
# ll.print_list()

# ll.delete_at_pos(2)
# ll.print_list()
#
# ll.delete_with_key(3)
# ll.print_list()
#
# ll.delete_with_key(0)
# ll.print_list()
#
# ll.delete_with_key(1)
# ll.print_list()

# print ll.find_length(ll.head)
# ll.print_list()
#
# print ll.search_recursive(0, ll.head)
# print ll.search_recursive(5, ll.head)
# print ll.search_recursive(1, ll.head)
# print ll.search_recursive(-1, ll.head)

# ll.swap_nodes(0, 5)
ll.reverse(ll.head)
ll.print_list()

# print ll.get_nth_node(0)
# print ll.get_nth_node(4)
# print ll.get_nth_node(5)
# print ll.get_nth_node(6)
# print ll.get_nth_node(-1)

# ll.print_list()
# ll.delete_list()
# ll.print_list()


# print ll.get_middle()
# ll.delete_at_pos(0)
# ll.print_list()
# print ll.get_middle()
# ll.delete_at_pos(0)
# ll.print_list()
# print ll.get_middle()
# ll.delete_at_pos(0)
# ll.print_list()
# print ll.get_middle()
# ll.delete_at_pos(0)
# ll.print_list()
# print ll.get_middle()
# ll.delete_at_pos(0)
# ll.print_list()
# print ll.get_middle()
# ll.delete_at_pos(0)
# ll.print_list()
# print ll.get_middle()
#
# print ll.get_nth_node_from_end(0)
# print ll.get_nth_node_from_end(7)
# print ll.get_nth_node_from_end(1)
# print ll.get_nth_node_from_end(6)
# print ll.get_nth_node_from_end(5)
# print ll.get_nth_node_from_end(3)

# ll.reverse(ll.head)

# set and check loop
# ll.print_list()
# ll.set_loop(44)
# print ll.check_loop()


ll1 = LinkList()

# ll.insert_at_pos(0, 4)

# ll.print_list()
ll1.add(2)
ll1.add(4)
ll1.add(6)
# ll.print_list()
# print ll.get_length()

ll1.insert_at_end(0)
ll1.insert_at_end(-2)
ll1.reverse(ll1.head)
ll1.print_list()

# ll.print_list()

ll.merge_list(ll1.head)

ll.print_list()

