from linkedList.Node import Node


class Queue(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self, obj):
        temp = Node(obj)
        self.size += 1
        if self.size == 1:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    def deQueue(self):
        if self.size == 0:
            return None
        temp = self.front
        self.front = self.front.next
        self.size -= 1
        return temp

    def __len__(self):
        return self.size

