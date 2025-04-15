import os
import re
import nltk
import pymorphy2
from nltk.stem import WordNetLemmatizer
from collections import defaultdict

# Загрузка ресурсов NLTK
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("stopwords")
from nltk.corpus import stopwords

# Инициализация лемматизаторов
morph = pymorphy2.MorphAnalyzer()
lemmatizer = WordNetLemmatizer()

# Пути к папкам и файлам
ARTICLES_FOLDER = "downloaded_pages"
TOKENS_FOLDER = "tokens"
LEMMAS_FOLDER = "lemmas"

# Создание папок для токенов и лемм, если они не существуют
os.makedirs(TOKENS_FOLDER, exist_ok=True)
os.makedirs(LEMMAS_FOLDER, exist_ok=True)

# Объединённый список стоп-слов
RUSSIAN_STOPWORDS = {
    "и", "в", "во", "на", "с", "по", "за", "от", "до", "у", "о", "а", "но", "же", "что", "как", "бы", "это",
    "из", "для", "ли", "же", "быть", "к", "также", "тоже", "еще", "так", "не", "да", "ну"
}
ENGLISH_STOPWORDS = set(stopwords.words("english"))
STOPWORDS = RUSSIAN_STOPWORDS.union(ENGLISH_STOPWORDS)

# Очистка текста от HTML/JS и мусора
def clean_text(text):
    text = re.sub(r"<[^>]+>", " ", text)  # Удаление HTML-тегов
    text = re.sub(r"(?i)\b(function|var|let|const|return|document|window|onclick|script|console|log|alert)\b", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)  # Удаление пунктуации
    text = re.sub(r"\d+", " ", text)      # Удаление чисел
    text = text.lower()
    return text

# Проверка валидности токена
def is_valid_token(token):
    if len(token) < 2 or len(token) > 20:
        return False
    if "_" in token:
        return False
    if re.search(r"\d", token):  # Слова с цифрами
        return False
    if not re.match(r"^[a-zа-яё]+$", token):  # Только буквы
        return False
    if token in STOPWORDS:
        return False
    if "amp" in token or "lt" in token or "gt" in token:
        return False
    return True

# Определение языка токена
def is_russian(word):
    return bool(re.match(r"^[а-яё]+$", word))

# Лемматизация токена
def lemmatize(token):
    if is_russian(token):
        return morph.parse(token)[0].normal_form
    else:
        return lemmatizer.lemmatize(token)

# Обработка всех файлов
for filename in os.listdir(ARTICLES_FOLDER):
    if filename.endswith(".txt"):
        all_tokens = set()
        lemma_dict = defaultdict(set)

        # Открытие файла и очистка текста
        with open(os.path.join(ARTICLES_FOLDER, filename), "r", encoding="utf-8") as f:
            text = clean_text(f.read())
            words = text.split()

            # Токенизация и лемматизация
            for word in words:
                if is_valid_token(word):
                    all_tokens.add(word)
                    lemma = lemmatize(word)
                    lemma_dict[lemma].add(word)

        # Сохранение всех токенов для данного файла
        with open(os.path.join(TOKENS_FOLDER, f"{filename}_tokens.txt"), "w", encoding="utf-8") as f:
            for token in sorted(all_tokens):
                f.write(f"{token}\n")

        # Сохранение лемм и связанных токенов для данного файла
        with open(os.path.join(LEMMAS_FOLDER, f"{filename}_grouped_lemmas.txt"), "w", encoding="utf-8") as f:
            for lemma, tokens in sorted(lemma_dict.items()):
                token_line = " ".join(sorted(tokens))
                f.write(f"{lemma} {token_line}\n")

        print(f"Готово для файла {filename}: сохранены токены и леммы в папки.")
