filename = input("CSV name (e.g.,data):").strip() + "_Sorted.csv"

#send to pandas
import pandas as pd
df = pd.read_csv(filename)

#convert to float and strip the symbols again JIC
df["Grant Total"] = df["Grant Total"].astype(float)

#Group and sort in pandas
state_totals = df.groupby("State")["Grant Total"].sum().sort_values()

#Plot
import matplotlib.pyplot as plt
plt.style.use("ggplot")
state_totals.nlargest(15).plot(kind="bar", figsize=(5,6))
plt.xlabel("Total Grant ($)")
plt.title("IDEA Funding by State")
plt.tight_layout()

#output and display
plt.savefig("State_totals.svg")
plt.show()
