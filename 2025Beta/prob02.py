# simply grab all flashes
nums = []
while True:
    num = input()
    if num == "0":
        break
    nums.append(int(num))

# make a list of all odds
odds = []
for num in nums:
    if num % 2 != 0:
        odds.append(num)

# if there are any odds, print them and print FLASH FAILED otherwise print FLASH FORWARD
if len(odds) > 0:
    for odd in odds:
        print(f"{odd} is odd")
    print("FLASH FAILED")
else:
    print("FLASH FORWARD")