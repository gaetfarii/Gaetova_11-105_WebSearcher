import os
import re
from collections import defaultdict

LEMMAS_FOLDER = "../lemmas"
INVERTED_INDEX_FILE = "inverted_index.txt"

# Словарь: лемма -> множество документов
inverted_index = defaultdict(set)

# Обрабатываем каждый файл в папке lemmas
for filename in os.listdir(LEMMAS_FOLDER):
    if filename.endswith(".txt"):
        filepath = os.path.join(LEMMAS_FOLDER, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
                if parts:
                    lemma = parts[0]
                    inverted_index[lemma].add(filename)

# Сохраняем инвертированный индекс в файл
with open(INVERTED_INDEX_FILE, "w", encoding="utf-8") as file:
    for lemma in sorted(inverted_index):
        docs = " ".join(sorted(inverted_index[lemma]))
        file.write(f"{lemma}: {docs}\n")

print("Готово: файл inverted_index.txt создан.")
