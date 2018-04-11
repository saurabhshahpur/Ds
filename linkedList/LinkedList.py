class LinkedList():
    def __init__(self, data):
        self.data = data
        self.next = None

    def add(self, data, head):
        temp = LinkedList(data)
        temp.next = head
        head = temp
        return head

    def print_list(self, head):
        temp = head
        while temp:
            print (temp.data),
            temp = temp.next

    def print_reverse(self, head):
        if not head:
            return
        self.print_reverse(head.next)
        print (head.data),

    def insert_at_end(self, data, head):
        temp = LinkedList(data)
        if not head:
            return temp
        trav = head
        while trav.next:
            trav = trav.next
        trav.next = temp
        return head


head = LinkedList(6)
head = head.add(7, head)
# print ("before 8")
# print (hex(id(head)))
head = head.add(8, head)
# print (hex(id(head)))
# print ("after 8")
head = head.add(9, head)
head = head.add(10, head)
head = head.insert_at_end(5,head)
head.print_list(head)
print "\n"
head.print_reverse(head)
print "\n"
head.print_list(head)
