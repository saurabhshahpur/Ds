from graph.Vertex import Vertex
from queue.Queue import Queue


class Graph(object):
    def __init__(self):
        self.no_of_vertex = 0
        self.no_of_edge = 0
        self.vertices = {}

    def addVertex(self, u):
        new_vertex = Vertex(u)
        self.no_of_vertex += 1
        self.vertices[u] = new_vertex
        return new_vertex

    def getVertex(self, u):
        if u in self.vertices:
            return self.vertices[u]
        return None

    def addEdge(self, u, v, w=0):
        if u not in self.vertices:
            # create new vertex
            self.addVertex(u)
        if v not in self.vertices:
            self.addVertex(v)
        self.no_of_edge += 1
        self.vertices[u].addNeighbor(self.vertices[v], w)

    def getVertices(self):
        return self.vertices.keys()

    # |V|
    def getVertexSize(self):
        return self.no_of_vertex

    # |E|
    def getEdgeSize(self):
        return self.no_of_edge

    def __iter__(self):
        return iter(self.vertices.values())

    def BFS(self, key):
        q = Queue()
        vs = self.getVertices()
        if self.getVertexSize() == 0:
            return
        q.enQueue(vs[0])
        visited = {}
        for v in vs:
            visited[v] = False

        while not q.isEmpty():
            curr_v = q.deQueue()
            visited[curr_v] = True
            if curr_v == key:
                return True
            u = self.getVertex(curr_v)
            connections = u.getConnections()
            for v in connections:
                if not visited[v.getId()]:
                    q.enQueue(v.getId())
        return False


def main():
    pass


if __name__ == '__main__':
    main()
