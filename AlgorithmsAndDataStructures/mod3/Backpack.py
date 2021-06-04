import math
from functools import reduce

class BackpackSolver:
    def __init__(self, maxWeight):
        if maxWeight < 0:
            raise(Exception)

        self.maxWeight = maxWeight;
        self.stuff = []


    def add(self, weight, value):
        if weight < 0 or value < 0:
            raise(Exception)

        self.stuff.append([weight,value])


    def calcGCD(self):
        weightArr = [self.maxWeight]
        for i in self.stuff:
            weightArr.append(i[0])

        self.gcd = reduce(math.gcd, weightArr)

    def reduce_weights(self):      
        self.calcGCD()

        self.maxWeight = int(self.maxWeight / self.gcd)
        for i in self.stuff:
            i[0] = int(i[0] / self.gcd)

    def calcCost(self, i, j):
        woutCurrent = self.matrix[i - 1][j]

        cost = self.stuff[i - 1][1]
        weight = j - self.stuff[i - 1][0]
        if weight < 0:
            return woutCurrent

        wCurrent = cost + self.matrix[i - 1][weight]
        return max(wCurrent, woutCurrent)
        
    def algorithm(self):
        self.reduce_weights()

        rows = len(self.stuff) + 1
        cols = self.maxWeight + 1
        self.matrix = []
        for i in range(rows):
            self.matrix.append([0] * cols)

        for i in range(1, rows):
            for j in range(cols):
                self.matrix[i][j] = self.calcCost(i, j)

        chosenItems = []
        totalWeight = 0
        totalValue = 0

        i = rows - 1
        j = cols - 1
        while j >= 0 and i > 0:
            if self.matrix[i][j] != self.matrix[i - 1][j]:
                current = self.stuff[i - 1]
                j -= current[0]

                chosenItems.append(i)
                totalWeight += current[0]
                totalValue += current[1]

            i -= 1

        return chosenItems, totalWeight*self.gcd, totalValue


def emptyLine(line):
    line.replace(' ', '')
    if line:
        return False
    return True

cycle = True
backpack = None

while cycle:
    try:
        line = input()
        if emptyLine(line):
            continue 

        cmd = line.split(' ', 1)
        try:
            if not backpack:
                if len(cmd) == 1:
                    maxWeight = int(cmd[0])
                    backpack = BackpackSolver(maxWeight)

                else:
                    raise(Exception)

            else:
                if len(cmd) == 2:
                    weight = int(cmd[0])
                    value = int(cmd[1])
                    backpack.add(weight, value)

                else:
                    raise(Exception)

        except Exception:
            print('error')
            continue

    except Exception:
        cycle = False

        if backpack:
            items, weigth, value = backpack.algorithm()

            print(weigth, value)
            for i in range(len(items) - 1, -1, -1):
                print(items[i])
