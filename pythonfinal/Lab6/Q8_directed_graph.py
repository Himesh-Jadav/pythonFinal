graph = {'A': ['B','C'], 'B': ['C'], 'C': ['A'], 'D': []}
nodes = set(graph)
for neighbors in graph.values():
    nodes.update(neighbors)
indeg, outdeg = {}, {}
for node in nodes:
    outdeg[node] = len(graph.get(node, []))
    indeg[node] = sum(node in neighbors for neighbors in graph.values())
print("In-degree:", indeg)
print("Out-degree:", outdeg)
# Jaccard similarity of two nodes' neighbor sets
a, b = input("Two nodes for Jaccard (e.g. A B): ").split()
s1, s2 = set(graph.get(a, [])), set(graph.get(b, []))
union = s1 | s2
print("Jaccard:", len(s1 & s2) / len(union) if union else 1)
