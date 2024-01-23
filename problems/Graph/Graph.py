class Vertex:
    def __init__(self, key) -> None:
        self.key = key
        self.neighbors = {}

    def get_neighbor(self, other):
        return self.neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        self.neighbors[other] = weight

    def __repr__(self) -> str:
        return f"Vertex({self.key})"

    def __str__(self) -> str:
        return f"{self.key} connected to: {[x.key for x in self.neighbors]}"

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key


class Graph:
    def __init__(self) -> None:
        self.vertices = {}

    def set_vertex(self, key) -> None:
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key) -> Vertex | None:
        return self.vertices.get(key, None)

    def __contains__(self, key) -> bool:
        return key in self.vertices

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self.vertices:
            self.set_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.set_vertex(to_vertex)
        self.get_vertex(from_vertex).set_neighbor(
            self.get_vertex(to_vertex), weight=weight
        )

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())


new_graph = Graph()
for i in range(6):
    new_graph.set_vertex(i)

print(new_graph.get_vertices())

new_graph.add_edge(0, 1, 5)
new_graph.add_edge(0, 5, 2)
new_graph.add_edge(1, 2, 4)
new_graph.add_edge(2, 3, 9)
new_graph.add_edge(3, 4, 7)
new_graph.add_edge(3, 5, 3)
new_graph.add_edge(4, 0, 1)
new_graph.add_edge(5, 4, 8)
new_graph.add_edge(5, 2, 1)

print(new_graph.get_vertex(1))
for v in new_graph:
    for w in v.get_neighbors():
        print(f"({v.get_key()}, {w.get_key()})")
        print(v.get_neighbors())
