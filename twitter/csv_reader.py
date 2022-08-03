import random
import pandas as pd


def get_random_keywords(source, column_name,words_count):

    df = pd.read_csv(source)
    lis = df[column_name].to_list()
    return random.choices(lis, k=words_count)


def get_all_keywords(source, column_name):

    df = pd.read_csv(source)
    lis = df[column_name].to_list()
    return lis