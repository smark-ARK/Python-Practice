from pythonds3.graphs import Graph
from bfs import bfs


def build_graph(path):
    buckets = {}
    g = Graph()
    with open(path, "r") as file_in:
        all_words = file_in.readlines()
    for line in all_words:
        word = line.strip()
        for i, _ in enumerate(word):
            bucket = f"{word[:i]}_{word[i+1:]}"
            buckets.setdefault(bucket, set()).add(word)
    for similar_words in buckets.values():
        for word1 in similar_words:
            for word2 in similar_words - {word1}:
                g.add_edge(word1, word2)
    return g


word_graph = build_graph(
    "/home/ark/programming/learning/Python-Practice/problems/Graph/words.txt"
)

# for v in word_graph:
#     for w in v.get_neighbors():
#         print(f"({v.get_key()}, {w.get_key()})")


res = bfs(word_graph.get_vertex("cove"), "sank")
print(res.distance)


def traverse(starting_vertex):
    current = starting_vertex
    while current:
        print(current.key)
        current = current.previous


traverse(word_graph.get_vertex("sank"))
