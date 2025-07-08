"""  
Grant_Sorter.py  
Reads a CSV of IDEA grant data, extracts state totals, and saves a sorted list.  
"""  
import csv

# get user input and  add .csv so you don't have to type it
filename = input("Enter CSV filename (e.g., file1.csv): ").strip()
if not filename.endswith(".csv"):
    filename += ".csv"

# read and sort the csv file, strip grant totals to convert to float
states_grants = []
with open(filename, newline="") as f:
    for row in csv.DictReader(f):
        state = row["State"]
        grant = float(row["Grant Total"].replace("$", "").replace(",", ""))
        states_grants.append((state, grant))
        
#store sorted list to be saved in new file
sorted_data = sorted(states_grants, key=lambda p: p[1])

#create the new file with "_Sorted"
new_filename = (filename[:-4] if filename.endswith(".csv") else filename) + "_Sorted.csv"
with open(new_filename, "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["State", "Grant Total"])
    for state, grant in sorted_data:
        writer.writerow([state, f"{grant:.2f}"])
        
#confirmation of new saved file
print(f"Sorted data saved to {new_filename}")
