# I forgor to keep part 1
def isHorizontal(startPoint, endPoint):
    return startPoint[0] == endPoint[0] or startPoint[1] == endPoint[1]


def isDiagonal(startPoint, endPoint):
    return abs(startPoint[0] - endPoint[0]) == abs(startPoint[1] - endPoint[1])


def getOffset(startPoint, endPoint):
    offset = [2*int(bin(startPoint[0] < endPoint[0]), 2)-1,
              2*int(bin(startPoint[1] < endPoint[1]), 2)-1]
    if startPoint[0] == endPoint[0]:
        offset[0] = 0
    elif startPoint[1] == endPoint[1]:
        offset[1] = 0
    return offset


def getDifference(startPoint, endPoint):
    if isHorizontal(startPoint, endPoint):
        return int(((startPoint[0]-endPoint[0])**2 + (startPoint[1]-endPoint[1])**2)**0.5)+1
    else:
        return abs(startPoint[0] - endPoint[0]) + 1


class Cell:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def getValue(self):
        ret = self.value
        if ret == 0:
            ret = "."
        return ret


class Table:
    def __init__(self):
        self.rows = list()
        self.size = 3
        self.cellsAbove1 = 0
        for i in range(self.size):
            self.rows.append(list())
            for j in range(self.size):
                self.rows[i].append(Cell())

    def print(self):
        print(self.cellsAbove1)
        return
        for row in self.rows:
            for cell in row:
                print(cell.getValue(), end=" ")
            print()

    def expand(self, size):
        for i in range(size-self.size):
            self.rows.append(list())
        self.size = size
        for i in range(self.size):
            for j in range(self.size - len(self.rows[i])):
                self.rows[i].append(Cell())

    def adjustSize(self, startPoint, endPoint):
        highest = 0
        for value in startPoint + endPoint:
            value += 1
            if value > highest:
                highest = value
        if highest > self.size:
            self.expand(highest)

    def mark(self, line):
        line = line.split(" -> ")
        startPoint = line[0].split(",")
        for i in range(len(startPoint)):
            startPoint[i] = int(startPoint[i])
        endPoint = line[1].split(",")
        for i in range(len(endPoint)):
            endPoint[i] = int(endPoint[i])
        if isHorizontal(startPoint, endPoint) or isDiagonal(startPoint, endPoint):
            self.adjustSize(startPoint, endPoint)
            offset = getOffset(startPoint, endPoint)
            for i in range(getDifference(startPoint, endPoint)):
                self.markCell(startPoint)
                startPoint[0] += offset[0]
                startPoint[1] += offset[1]

    def markCell(self, point):
        cell = self.getCell(int(point[1]), int(point[0]))
        cell.inc()
        if cell.getValue() == 2:
            self.cellsAbove1 += 1

    def getCell(self, x, y):
        return self.rows[x][y]


class Main:
    def __init__(self):
        self.table = Table()
        file = open("input.in", "r")
        lines = file.read()[:-1].split("\n")
        file.close()
        for line in lines:
            self.table.mark(line)
        self.table.print()


Main()
