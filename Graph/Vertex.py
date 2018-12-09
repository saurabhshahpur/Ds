class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def addNeighbor(self, nbr, w=0):
        self.connected_to[nbr] = w

    def getWeight(self, nbr):
        return self.connected_to[nbr]

    def getId(self):
        return self.id

    def getConnections(self):
        return self.connected_to.keys()
