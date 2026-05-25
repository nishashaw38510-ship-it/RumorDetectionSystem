import pandas as pd
import random

def fetch_social_posts():

    df = pd.read_csv('dataset/rumor_dataset.csv')

    sample_posts = df.sample(5)

    posts = []

    for _, row in sample_posts.iterrows():

        posts.append({
            "platform": row['platform'],
            "username": row['username'],
            "post": row['post'],
            "date": row['date']
        })

    return posts