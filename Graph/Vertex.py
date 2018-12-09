class Vertex(object):
    def __init__(self, key):  # O(1)
        self.id = key
        self.connected_to = {}

    def addNeighbor(self, nbr, w=0):  # O(1)
        self.connected_to[nbr] = w

    def getWeight(self, nbr):  # O(1)
        return self.connected_to[nbr]

    def getId(self):  # O(1)
        return self.id

    def getConnections(self):   # O(n) where n is the number of node which are connected to this
        return self.connected_to.keys()
