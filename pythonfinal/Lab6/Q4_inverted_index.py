docs = {'doc1': 'python list tuple', 'doc2': 'python dictionary', 'doc3': 'list dictionary'}
index = {}
for doc, text in docs.items():
    for word in text.lower().split():
        index.setdefault(word, []).append(doc)
query = input("Search word: ").lower()
print("Documents:", index.get(query, []))
