from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def similarity_score(base_document):
    vectorizer = TfidfVectorizer()

    df = pd.read_csv('label_learning.csv')

    df['title_snippet'] = df['title'] + df['snippet']

    documents = df['title_snippet'].tolist()

    documents.insert(0, base_document)
    embeddings = vectorizer.fit_transform(documents)

    cosine_similarities = cosine_similarity(
        embeddings[0:1], embeddings[1:]).flatten()

    highest_score = 0
    highest_score_index = 0

    lowest_score = 100
    lowest_score_index = 0
    for i, score in enumerate(cosine_similarities):
        if highest_score < score:
            highest_score = score
            highest_score_index = i
        if lowest_score > score:
            lowest_score = score
            lowest_score_index = i

    most_similar_document = documents[highest_score_index]
    least_similar_document = documents[lowest_score_index]

    print("Most similar document by TF-IDF with the score:",
          most_similar_document, highest_score)

    print("Least similar document by TF-IDF with the score: ",
          least_similar_document, lowest_score)
    print(embeddings[0:2])


similarity_score(
    "Learn how to play chords at lightning speed, three strumming secrets, pick technique, and get tips for tuning and practice time. Here's a FREE guide.")
