file = open("input.in", "r")
lines = file.read().split("\n")[:-1]
file.close()
for i in range(len(lines)):
    lines[i] = int(lines[i])

increases = 0

for i in range(len(lines)-3):
    if lines[i] + lines[i+1] + lines[i+2] < lines[i+1] + lines[i+2] + lines[i+3]:
        increases += 1
print(increases)
