import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("average_each_month.csv")

labels = data["formatted_month"]
values = data["round"]

plt.bar(labels, values)

plt.xlabel("Rating")
plt.ylabel("Month")
plt.title("Monthly Average Review Ratings")
plt.tight_layout()

plt.show()
