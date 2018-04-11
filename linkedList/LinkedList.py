# import bpy
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
            print id(temp)
            temp = temp.next
        print "\n"

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

    def insert_after_key(self, data, key, head):
        temp_i = LinkedList(data)
        if not head:
            return "error"
        temp = head
        while temp.data != key:
            temp = temp.next

        temp_i.next = temp.next
        temp.next = temp_i
        return head

    def insert_at_position(self, data, position, head):
        temp_i = LinkedList(data)
        temp = head
        while position > 2:
            temp = temp.next
            position -= 1

        temp_i.next = temp.next
        temp.next = temp_i
        return head

    def length(self, head):
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        return count

    def delete_first(self, head):
        temp = head.next
        del head
        return temp

    # def __del__(self):
    #     class_name = self.__class__.__name__
    #     print class_name, "destroyed"

    def delete_last(self, head):
        # print "\n"
        temp = head
        prev = None
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        del temp

        return head


# create list
head = LinkedList(6)

# insert at head
head = head.add(7, head)
head = head.add(8, head)
head = head.add(10, head)
head = head.add(11, head)

# insert at end
head = head.insert_at_end(5, head)

# print list
head.print_list(head)

# insert after key
head = head.insert_after_key(9, 10, head)
head.print_list(head)

# insert at pos
head = head.insert_at_position(20, 8, head)
head.print_list(head)


# delete head
head = head.delete_first(head)
head.print_list(head)
head = head.insert_after_key(11, 10, head)
head = head.delete_first(head)
head = head.insert_after_key(10, 11, head)
head.print_list(head)

# delete last
head = head.delete_last(head)

head.print_list(head)

