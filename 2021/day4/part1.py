class Cell:
    def __init__(self, value):
        self.value = value
        self.marked = False


class Table:
    def __init__(self, line):
        self.values = list()
        for row in line.split("\n"):
            row = row.strip().replace("  ", " ").split(" ")
            for i in range(len(row)):
                row[i] = Cell(int(row[i]))
            self.values.append(row)

    def markCell(self, value):
        for row in self.values:
            for cell in row:
                if cell.value == value:
                    cell.marked = True

    def isWinner(self):
        for row in self.values:
            rowLength = len(row)
            for cell in row:
                rowLength -= int(bin(cell.marked), 2)
            if rowLength == 0:
                raise True
        for index in range(len(self.values[0])):
            columnLength = len(self.values[0])
            for row in self.values:
                cell = row[index]
                columnLength -= int(bin(cell.marked), 2)
            if columnLength == 0:
                raise True
        return False

    def getUnmarked(self):
        sum = 0
        for row in self.values:
            for cell in row:
                if not cell.marked:
                    sum += cell.value
        return sum


class Main:
    def __init__(self):
        file = open("input.in", "r")
        lines = file.read()[:-1].split("\n\n")
        file.close()

        numbers = lines[0].split(",")

        self.tables = list()
        for line in lines[1:]:
            self.tables.append(Table(line))
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        for number in numbers:
            for table in self.tables:
                table.markCell(number)
                if table.isWinner():
                    print(int(table.getUnmarked()) * number)
                    return


Main()
