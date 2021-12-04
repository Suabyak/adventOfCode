file = open("input.in", "r")
lines = file.read().split("\n")[:-1]
file.close()


class submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.__move = {"down": self.moveDown, "forward": self.moveForward,
                       "up": self.moveUp}

    def move(self, line):
        line = line.split(" ")
        line[1] = int(line[1])
        self.__move[line[0]](line[1])

    def moveUp(self, distance):
        self.depth -= distance

    def moveDown(self, distance):
        self.depth += distance

    def moveForward(self, distance):
        self.horizontal += distance

    def __str__(self):
        return str(self.horizontal * self.depth)


sub = submarine()

for line in lines:
    sub.move(line)
print(sub)
