file = open("input.in", "r")
lines = file.read().split("\n")[:-1]
file.close()


class Submarine:
    def __init__(self):
        self.numbers = dict()

    def run(self, lines):
        for line in lines:
            for i in range(len(line)):
                char = 2 * int(line[i]) - 1
                try:
                    self.numbers[i] += char
                except:
                    self.numbers[i] = char

    def getAnswer(self):
        gamma = ""
        epsilon = ""
        for _, var in self.numbers.items():
            gamma += bin(var > 0)
            epsilon += bin(var < 0)
        gamma = int(gamma.replace("0b", ""), 2)
        epsilon = int(epsilon.replace("0b", ""), 2)
        return (gamma, epsilon, gamma * epsilon)


submarine = Submarine()
submarine.run(lines)
print(submarine.getAnswer())
