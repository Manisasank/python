def term_frequency(text: str) -> dict:
    words = text.lower().replace('.', '').split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
sample_text = "machine learning empowers AI. learning Python drives machine intelligence."
print(f"Frequencies: {term_frequency(sample_text)}")