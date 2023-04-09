import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file into a pandas DataFrame
df = pd.read_csv("income_data.csv")

# filter the DataFrame to keep only the relevant rows
df = df[df["GEO"] == "Canada"]
df = df[df["Family type"].isin(["Couple families", "Lone-parent families"])]
df = df[df["Age of older adult"] == "Total all ages"]
df = df[df["Family income"] == "Median total income"]

# pivot the DataFrame to put the years in columns
df = df.pivot(index="Family type", columns="REF_DATE", values="VALUE")

# plot the data using a bar chart
ax = df.plot(kind="bar", rot=0)
ax.set_xlabel("Family Type")
ax.set_ylabel("Median Income (CAD)")
ax.set_title("Median Income in Canada vs Family Type")
plt.show()
