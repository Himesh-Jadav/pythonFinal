# Piglet-style conversion: move first letter to end + 'ho'
sentence = input("Enter sentence: ")
words = sentence.split()
piglet = [w[1:] + w[0] + "ho" if len(w) > 1 else w + "ho" for w in words]
print(" ".join(piglet))
