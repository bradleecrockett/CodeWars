from datetime import datetime, timedelta
import os

# grab vars
signal = input()
start = input()
stop = input()

# convert to datetime
start_date = datetime.strptime(start, "%Y-%m-%d")
temp_date = start_date
stop_date = datetime.strptime(stop, "%Y-%m-%d")

# store codes and fund variable
codes = []
funds = 0.0

while True:

    # make a string of the current date
    current = str(temp_date.date())

    # read the file if it exists
    if os.path.exists(f"{current}.txt"):
        with open(f"{current}.txt", "r") as file:
            lines = file.read().split('\n')
            file.close()
        
        # iterate through the lines and parse the data to see if values match
        for line in lines:
            line = line.split(',')
            if line[-1] != signal: continue

            funds += float(line[-2])
            codes.append(line[0])
    # increment the date
    temp_date += timedelta(days=1)
    
    # check if we are done
    if current == str(stop_date.date()):
        break

# print the codes and funds sorted
codes.sort()
for code in codes: print(code)
print(f"Funds Found: {funds}")