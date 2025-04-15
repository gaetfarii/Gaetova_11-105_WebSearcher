import os
import math
from collections import defaultdict

TOKENS_FOLDER = "tokens"
LEMMAS_FOLDER = "lemmas"
ARTICLES_FOLDER = "downloaded_pages"
TF_IDF_TERMS_FOLDER = "tf_idf_terms"
TF_IDF_LEMMAS_FOLDER = "tf_idf_lemmas"

# Создание папок для результатов
os.makedirs(TF_IDF_TERMS_FOLDER, exist_ok=True)
os.makedirs(TF_IDF_LEMMAS_FOLDER, exist_ok=True)

# Получение списка документов
documents = [f for f in os.listdir(TOKENS_FOLDER) if f.endswith("_tokens.txt")]
doc_count = len(documents)

# Словарь для подсчета df по терминам и леммам
df_terms = defaultdict(int)
df_lemmas = defaultdict(int)

# Словари для хранения tf по документам
tf_terms_per_doc = {}
tf_lemmas_per_doc = {}

# Подсчет tf и df
for doc in documents:
    with open(os.path.join(TOKENS_FOLDER, doc), "r", encoding="utf-8") as f:
        tokens = [line.strip() for line in f.readlines() if line.strip()]
    total_tokens = len(tokens)
    term_freq = defaultdict(int)
    for token in tokens:
        term_freq[token] += 1
    tf_terms = {term: freq / total_tokens for term, freq in term_freq.items()}
    tf_terms_per_doc[doc] = tf_terms
    for term in tf_terms:
        df_terms[term] += 1

    lemma_doc_name = doc.replace("_tokens.txt", "_grouped_lemmas.txt")
    with open(os.path.join(LEMMAS_FOLDER, lemma_doc_name), "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    lemma_freq = {}
    for line in lines:
        parts = line.split()
        lemma = parts[0]
        forms = parts[1:]
        total_forms = sum(term_freq.get(form, 0) for form in forms)
        if total_forms > 0:
            lemma_freq[lemma] = total_forms / total_tokens
            df_lemmas[lemma] += 1
    tf_lemmas_per_doc[doc] = lemma_freq

# Вычисление idf
idf_terms = {term: math.log(doc_count / df_terms[term]) for term in df_terms}
idf_lemmas = {lemma: math.log(doc_count / df_lemmas[lemma]) for lemma in df_lemmas}

# Сохранение результатов
for doc in documents:
    base_name = doc.replace("_tokens.txt", "")
    tf_terms = tf_terms_per_doc[doc]
    tf_lemmas = tf_lemmas_per_doc[doc]

    # Термины
    with open(os.path.join(TF_IDF_TERMS_FOLDER, f"{base_name}_tfidf_terms.txt"), "w", encoding="utf-8") as f:
        for term in sorted(tf_terms):
            idf = idf_terms.get(term, 0)
            tfidf = tf_terms[term] * idf
            f.write(f"{term} {idf:.6f} {tfidf:.6f}\n")

    # Леммы
    with open(os.path.join(TF_IDF_LEMMAS_FOLDER, f"{base_name}_tfidf_lemmas.txt"), "w", encoding="utf-8") as f:
        for lemma in sorted(tf_lemmas):
            idf = idf_lemmas.get(lemma, 0)
            tfidf = tf_lemmas[lemma] * idf
            f.write(f"{lemma} {idf:.6f} {tfidf:.6f}\n")
