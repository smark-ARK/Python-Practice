from Graph import Graph


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
