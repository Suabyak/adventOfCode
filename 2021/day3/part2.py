

class Submarine:
    def __init__(self):
        self.load()

    def load(self):
        global cont
        file = open("input.in", "r")
        cont = file.read().split("\n")[:-1]
        file.close()

    def getOxygen(self, lines, index=0):
        self.numbers = dict()
        for line in lines:
            for i in range(len(line)):
                char = 2 * int(line[i]) - 1
                try:
                    self.numbers[i] += char
                except:
                    self.numbers[i] = char
        toKeep = str(bin(self.numbers[index] >= 0)).replace("0b", "")
        deleted = 0
        for i in range(len(lines)):
            i = len(lines) - 1 - i + deleted
            if lines[i][index] != toKeep:
                lines.pop(i)
                deleted += 1
        if len(lines) == 1:
            self.oxygenRatio = int(lines[0], 2)
            return
        self.getOxygen(lines, index + 1)

    def getCo2(self, lines, index=0):
        self.numbers = dict()
        for line in lines:
            for i in range(len(line)):
                char = 2 * int(line[i]) - 1
                try:
                    self.numbers[i] += char
                except:
                    self.numbers[i] = char
        toDelete = str(bin(self.numbers[index] >= 0)).replace("0b", "")
        deleted = 0
        for i in range(len(lines)):
            i = len(lines) - 1 - i + deleted
            if lines[i][index] == toDelete:
                lines.pop(i)
                deleted += 1
        if len(lines) == 1:
            self.Co2Ratio = int(lines[0], 2)
            return
        self.getCo2(lines, index + 1)

    def getAnswer(self):
        return self.oxygenRatio * self.Co2Ratio


submarine = Submarine()
submarine.getOxygen(cont)
submarine.load()
submarine.getCo2(cont)
print(submarine.getAnswer())
