def term_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        word = word.strip(".,!?")
        freq[word] = freq.get(word, 0) + 1
    return freq
corpus = "the model learns from the data and the data guides the model"
tf = term_frequency(corpus)
for word, count in sorted(tf.items(), key=lambda item: -item[1]):
    print(f"{word:10s} -> {count}")