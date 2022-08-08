import random
from turtle import title
import pandas as pd
import csv
from os.path import exists

from tfidf_model import top10_similarity_score


def get_page(pages):
    idx = 0
    curScore = 0
    for i, page in enumerate(pages):
        totalScore = sum(top10_similarity_score(page))
        if totalScore > curScore:
            idx = i
            curScore = totalScore
    return pages[idx]


def store_info_in_csv(pages):
    column_names = ['title', 'snippet']
    required_data = []
    for page in pages:
        if 'snippet' in page and 'title' in page:
            required_data.append(
                [page['title'],  page['snippet']])

    file_exists = exists('search_results.csv')

    if file_exists:
        with open('search_results.csv', 'a+') as f:
            write = csv.writer(f)

            write.writerows(required_data)
        return

    with open('search_results.csv', 'w') as f:
        write = csv.writer(f)

        write.writerow(column_names)
        write.writerows(required_data)
