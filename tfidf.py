import numpy as np
import pandas as pd
import string
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
from stop_words import get_stop_words
stop_words = get_stop_words("russian")


def lemmatize_word(word):
    for s in string.punctuation:
        word = word.replace(s, "")
    morph_analyze = morph.parse(word.lower())
    return morph_analyze[0].normal_form


def lemmatize_text(text):
    if isinstance(text, str):
        text = text.split()
    normal_text = [lemmatize_word(w) for w in text if w not in stop_words]
    return normal_text


def tf(key, document):
    # Определяет частоту встречаемости слова в тексте
    normal_key = lemmatize_word(key)
    normal_doc = lemmatize_text(document)

    return normal_doc.count(normal_key) / len(normal_doc)


def tfidf(key, documents):
    # Ищет важность ключа относительно всех текстов для каждого из них
    normal_docs = [lemmatize_text(doc) for doc in documents]
    normal_key = lemmatize_text(key)

    result = [0 for i in range(len(normal_docs))]

    for word in normal_key:
        for item in range(len(normal_docs)):

            occurences = sum([1 for i in normal_docs if normal_key in i])
            result[item] += (tf(word, normal_docs[item]) * np.log2((len(normal_docs) + 1) / (occurences + 1)))

    return result


def get_relevant_words(text):
    normal_text = lemmatize_text(text)
    words = set(normal_text)
    result = [(w, tf(w, normal_text)) for w in words]
    return result


def choose_answer(key):
    relevance = tfidf(key, texts)
    answer_index = relevance.index(max(relevance))
    return texts[answer_index]


texts = [open("texts/" + str(name), "r").read() for name in range(1, 18)]
