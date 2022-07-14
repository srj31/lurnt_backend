import random
from tkinter import W
from turtle import title
import pandas as pd
import csv
from os.path import exists


def get_page(pages):
    random_index = random.randint(0, 10)
    return pages[random_index]


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
