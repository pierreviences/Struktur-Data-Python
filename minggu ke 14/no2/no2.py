
print("Nama 	: Muhamad yazid Imani ")
print("NIM 	: J0303211068 ")
print("Prodi 	: Manajemen Informatika ")

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(9)
g.add_edge(0, 1, 8)
g.add_edge(0, 2, 12)
g.add_edge(1, 2, 13)
g.add_edge(1, 3, 25)
g.add_edge(1, 4, 9)
g.add_edge(2, 3, 14)
g.add_edge(2, 6, 21)
g.add_edge(3, 4, 20)
g.add_edge(3, 5, 8)
g.add_edge(3, 6, 12)
g.add_edge(3, 7, 12)
g.add_edge(3, 8, 16)
g.add_edge(4, 5, 19)
g.add_edge(5, 7, 11)
g.add_edge(6, 8, 11)
g.add_edge(7, 8, 9)
g.kruskal_algo()
