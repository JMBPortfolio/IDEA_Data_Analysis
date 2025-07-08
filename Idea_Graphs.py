filename = input("CSV name (e.g.,data):").strip() + "_Sorted.csv"

#send to pandas
import pandas as pd
df = pd.read_csv(filename)

#convert to float and strip the symbols again JIC (want to make sure it's able to convert to float)
df["Grant Total"] = df["Grant Total"].astype(float)

#Group and sort in pandas
df = df[df["State"] != "US Total" ]
state_totals = df.groupby("State")["Grant Total"].sum().sort_values()

#Plot
import matplotlib.pyplot as plt
plt.style.use("ggplot")
state_totals.nlargest(25).plot(kind="bar", figsize=(5,6))
plt.xlabel("Total Grant ($)")
plt.title("IDEA Funding by State")
plt.tight_layout()

#output as {filename}_plot.svg
import os

stem = os.path.splitext(filename)[0]
plt.savefig(f"{stem}_plot.svg")

#Display
plt.show()
