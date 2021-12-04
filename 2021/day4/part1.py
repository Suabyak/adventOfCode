class Cell:
    def __init__(self):
        pass


class Table:
    def __init__(self, line):
        self.values = list()
        for row in line.split("\n"):
            row = row.strip().replace("  ", " ").split(" ")
            self.values.append(row)
        print(self.values, "\n")


class Main:
    def __init__(self):
        file = open("input.in", "r")
        lines = file.read()[:-1].split("\n\n")
        file.close()

        numbers = lines[0].split(",")

        self.tables = list()
        for line in lines[1:]:
            self.tables.append(Table(line))
        print(numbers)


Main()
