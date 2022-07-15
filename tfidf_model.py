from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import re
import string
from nltk.stem import PorterStemmer

ps = PorterStemmer()


def preprocess_documents(documents):
    preprocessed_documents = []
    i = 1
    for document in documents:
        document = document.lower()
        document = document.strip()
        document = re.compile('<.*?>').sub('', document)
        document = re.compile('[%s]' % re.escape(
            string.punctuation)).sub(' ', document)

        document = re.sub('\s+', ' ', document)
        document = re.sub(r'[^\w\s]', '', str(document).lower().strip())
        if i == 1:
            print(document)
        words = list(document.split(" "))
        words = [ps.stem(word) for word in words]

        document = ' '.join(words)
        if i == 1:
            print(document)

        document = re.sub(r'\d', ' ', document)
        document = re.sub(r'\s+', ' ', document)
        preprocessed_documents.append(document)
        i += 1
    return preprocessed_documents


def similarity_score(vectorizer, base_document):

    df = pd.read_csv('label_learning.csv')

    df['title_snippet'] = df['title'] + " " + df['snippet']

    documents = df['title_snippet'].tolist()

    documents.insert(0, base_document)
    documents = preprocess_documents(documents)
    embeddings = vectorizer.fit_transform(documents)

    cosine_similarities = cosine_similarity(
        embeddings[0:1], embeddings[1:]).flatten()

    highest_score = 0
    highest_score_index = 0

    zero_score_documents = []
    for i, score in enumerate(cosine_similarities):
        if highest_score < score:
            highest_score = score
            highest_score_index = i+1
        if score == 0:
            zero_score_documents.append(documents[i])

    most_similar_document = documents[highest_score_index]

    print("Most similar document by TF-IDF with the score:",
          most_similar_document, highest_score)


tf_idf_vectorizor = TfidfVectorizer()
count_vectorizor = CountVectorizer()


print("\033[1;32;40m --------------------------- this is Count-Vectorizer ----------------------------------------------------- \033[0;37;40m ")


similarity_score(tf_idf_vectorizor, "intermediate drum lessons")
