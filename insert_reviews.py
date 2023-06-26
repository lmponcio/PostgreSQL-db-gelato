import random
import sys
from datetime import datetime, timedelta

sys.setrecursionlimit(2000)


def generate_random_review():
    today = datetime.today()
    one_year_ago = today - timedelta(days=365)
    random_date = today - timedelta(days=random.randint(0, 365))
    random_review = random.randint(1, 5)
    random_icecream_id = random.randint(1, 37)

    random_date_str = random_date.strftime("%Y-%m-%d")

    return random_review, random_date_str, random_icecream_id


with open("insert_reviews.sql", "w") as file:
    for id in range(1, 200):
        this_review = generate_random_review()

        this_statement = f"""INSERT INTO review VALUES (
        {id},
        '{this_review[0]}',
        '{this_review[1]}',
        {this_review[2]}
        );"""
        file.write(this_statement + "\n")
