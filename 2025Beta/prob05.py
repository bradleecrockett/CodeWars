sep = input()
string = input()
result: str = ""

# split string by seperator and then reverse the list
string = string.split(sep)
string.reverse()

# concatenate the string with the seperator
for part in string:
    result += f"{part}{sep}"

# remove the last seperator
print(result[:-len(sep)])