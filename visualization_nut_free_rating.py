import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("average_nut_free.csv")
# reversing order for cosmetic purposes
data = data.iloc[::-1]

labels = data["name"]
values = data["average_rating"]

plt.barh(labels, values)

plt.xlabel("Average Review Rating")
plt.ylabel("Gelato Name")
plt.title("Nut Free Gelato Average Ratings")
plt.tight_layout()

plt.show()
