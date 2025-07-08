import csv

#Prompt user for file name
filename = input("Enter the CSV filename(e.g., file1.csv): ").strip()
#make sure format is correct
if not filename.endswith(".csv"):
    filename += ".csv"
#open the csv file and assign it to reader
with open(filename, newline="") as file:
    reader = csv.DictReader(file)
    #create list to store State name and grant amount
    states_grants = []
    #for each row in reader, get the state and grant value
    for row in reader:
        state = row["State"]
        grant = float(row["Grant Total"].replace("$","").replace(",",""))
        #store these values in states_grants
        states_grants.append((state,grant))
    #create a temporary list for each "state, grant" pair, sort by grants
    for state, grant in sorted(states_grants, key = lambda pair: pair[1]):
        #print "state: $grant"
        print(f"{state}: ${grant:,.2f}")
