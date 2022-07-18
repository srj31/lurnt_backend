from numpy import vectorize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import re
import string
from nltk.stem import PorterStemmer
from heapq import heappush, heappushpop

ps = PorterStemmer()


def preprocess_documents(documents):
    preprocessed_documents = []
    for document in documents:
        document = document.lower()
        document = document.strip()
        document = re.compile('<.*?>').sub('', document)
        document = re.compile('[%s]' % re.escape(
            string.punctuation)).sub(' ', document)

        document = re.sub('\s+', ' ', document)
        document = re.sub(r'[^\w\s]', '', str(document).lower().strip())
        words = list(document.split(" "))
        words = [ps.stem(word) for word in words]

        document = ' '.join(words)

        document = re.sub(r'\d', ' ', document)
        document = re.sub(r'\s+', ' ', document)
        preprocessed_documents.append(document)
    return preprocessed_documents


def top10_similarity_score(page):
    vectorizer = TfidfVectorizer()
    base_document = page['title'] + ' ' + page['snippet']
    df = pd.read_csv('label_learning.csv')

    df_learning_data = df.loc[(df['is_tutorial'] == 1)]

    df_learning_data['title_snippet'] = df_learning_data['title'] + \
        " " + df_learning_data['snippet']

    documents = df_learning_data['title_snippet'].tolist()

    documents.insert(0, base_document)
    documents = preprocess_documents(documents)
    embeddings = vectorizer.fit_transform(documents)

    cosine_similarities = cosine_similarity(
        embeddings[0:1], embeddings[1:]).flatten()

    heap = []
    for i, score in enumerate(cosine_similarities):
        if len(heap) < 10:
            heappush(heap, score)
        else:
            heappushpop(heap, score)

    return heap
