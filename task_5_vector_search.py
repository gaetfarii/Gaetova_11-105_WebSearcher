import os
import math
from collections import Counter
import re
from urls import urls

TF_IDF_LEMMAS_FOLDER = "tf_idf_lemmas"
LEMMAS_FOLDER = "lemmas"


documents = [f for f in os.listdir(TF_IDF_LEMMAS_FOLDER) if f.endswith("_tfidf_lemmas.txt")]

# TF-IDF векторы документов
doc_vectors = {}
idf = {}
for filename in documents:
    vector = {}
    with open(os.path.join(TF_IDF_LEMMAS_FOLDER, filename), "r", encoding="utf-8") as f:
        for line in f:
            lemma, idf_val, tfidf = line.strip().split()
            vector[lemma] = float(tfidf)
            if lemma not in idf:
                idf[lemma] = float(idf_val)
    doc_vectors[filename] = vector

# Функция косинусного сходства
def cosine_similarity(vec1, vec2):
    common_keys = set(vec1) & set(vec2)
    dot_product = sum(vec1[k] * vec2[k] for k in common_keys)
    norm1 = math.sqrt(sum(v ** 2 for v in vec1.values()))
    norm2 = math.sqrt(sum(v ** 2 for v in vec2.values()))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot_product / (norm1 * norm2)

# Получение формы, лемма
form_to_lemma = {}
for file in os.listdir(LEMMAS_FOLDER):
    if file.endswith("_grouped_lemmas.txt"):
        with open(os.path.join(LEMMAS_FOLDER, file), "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if parts:
                    lemma, forms = parts[0], parts[1:]
                    for form in forms:
                        form_to_lemma[form] = lemma

query = input("Введите поисковый запрос: ").strip().lower()
query_tokens = query.split()

# Проебразование токенов в леммы
query_lemmas = [form_to_lemma.get(token, token) for token in query_tokens]
print(f"Леммы запроса: {query_lemmas}")

# Подсчёт tf
query_tf = Counter(query_lemmas)
total = sum(query_tf.values())
query_vector = {}
for lemma in query_tf:
    if lemma in idf:
        tf = query_tf[lemma] / total
        query_vector[lemma] = tf * idf[lemma]

else:
    # Вычисление схожести
    scores = []
    for filename, vec in doc_vectors.items():
        sim = cosine_similarity(query_vector, vec)
        scores.append((filename, sim))

    scores.sort(key=lambda x: x[1], reverse=True)

    found = False
    for fname, score in scores:
        if score > 0:
            found = True
            print(f"{fname}: релевантность {score:.4f}")
            match = re.search(r'page_(\d+)\.txt', fname)
            if match:
                page_number = int(match.group(1))
                print(f"URL: {urls[page_number]}")

    if not found:
        print("По запросу ничего не найдено.")
