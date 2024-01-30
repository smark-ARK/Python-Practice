from pythonds3.basic import Queue
from pythonds3.graphs import Vertex


def bfs(start: Vertex, key: str) -> Vertex:
    start.distance = 0
    start.previous = None
    q = Queue()
    q.enqueue(start)
    while q.size() > 0:
        current = q.dequeue()
        for neighbor in current._neighbors:
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.distance = current.distance + 1
                neighbor.previous = current
                if neighbor.key == key:
                    return neighbor
                q.enqueue(neighbor)
        current.color = "black"
