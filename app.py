from flask import Flask, request, render_template
import os
import math
from collections import Counter
import re
from urls import urls

app = Flask(__name__)

TF_IDF_LEMMAS_FOLDER = "tf_idf_lemmas"
LEMMAS_FOLDER = "lemmas"

# Загрузка документов
documents = [f for f in os.listdir(TF_IDF_LEMMAS_FOLDER) if f.endswith("_tfidf_lemmas.txt")]

# Загрузка TF-IDF векторов и IDF
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

# Загрузка формы -> лемма
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

# Косинусное сходство
def cosine_similarity(vec1, vec2):
    common = set(vec1) & set(vec2)
    dot = sum(vec1[k] * vec2[k] for k in common)
    norm1 = math.sqrt(sum(v ** 2 for v in vec1.values()))
    norm2 = math.sqrt(sum(v ** 2 for v in vec2.values()))
    return dot / (norm1 * norm2) if norm1 and norm2 else 0.0

@app.route("/", methods=["GET", "POST"])
def search():
    results = []
    query = ""

    if request.method == "POST":
        query = request.form["query"].strip().lower()
        tokens = query.split()
        lemmas = [form_to_lemma.get(t, t) for t in tokens]

        query_tf = Counter(lemmas)
        total = sum(query_tf.values())
        query_vec = {}
        for lemma in query_tf:
            if lemma in idf:
                tf = query_tf[lemma] / total
                query_vec[lemma] = tf * idf[lemma]

        if not query_vec:
            results = []
        else:
            scores = []
            for fname, vec in doc_vectors.items():
                sim = cosine_similarity(query_vec, vec)
                if sim > 0:
                    match = re.search(r'page_(\d+)\.txt', fname)
                    if match:
                        page_id = int(match.group(1))
                        scores.append((urls[page_id], sim))

            scores.sort(key=lambda x: x[1], reverse=True)
            results = scores[:10]

    return render_template("index.html", results=results, query=query)

if __name__ == "__main__":
    app.run(debug=True)
