# read all lines
times = int(input())
lines = []
for i in range(times):
    lines.append(input())

# print all the lines in reverse
lines.reverse()
for line in lines:
    print(line)