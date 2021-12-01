file = open("input", "r")
lines = file.read().split("\n")[:-1]
file.close()
for i in range(len(lines)):
    lines[i] = int(lines[i])

sums = list()

increases = 0
for i in range(len(lines)-2):
    sums.append(lines[i]+lines[i+1]+lines[i+2])

for i in range(len(sums)-1):
    if sums[i] < sums[i+1]:
        increases += 1
print(increases)
