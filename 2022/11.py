from my_input import lines
import util
import math
import heapq

result = 0
monkeys =  []
inspected = []
dividers = []

class Monkey:
    def __init__(self):
        self.items = []
        self.opNum = ''
        self.opOp = ''
        self.test = -1
        self.true = -1
        self.false = -1

    def addItem(self, item):
        self.items.append(item)

    def operation(self, old):
        if self.opOp == '+':
            if self.opNum == 'old':
                return old + old
            else:
                return old + self.opNum
                
        if self.opOp == '*':
            if self.opNum == 'old':
                return old * old
            else:
                return old * self.opNum

    def worryLvl(self, idx):
        self.items[idx] = self.operation(self.items[idx])
        self.items[idx] %= math.lcm(*dividers)

    def doTest(self, idx):
        if self.items[idx] % self.test == 0:
            monkeys[self.true].addItem(self.items[idx])
        else:
            monkeys[self.false].addItem(self.items[idx])

# parse
for line in lines:
    if line.find('Monkey') >= 0:
        monkey = Monkey()
        monkeys.append(monkey)
        inspected.append(0)

    if line.find('Starting items:') >= 0:
        monkey.items = util.getNumbers(line, sep='')

    if line.find('Operation:') >= 0:
        if (len(util.getNumbers(line, sep='')) == 0):
            monkey.opNum = 'old'
        else:
            monkey.opNum = util.getNumbers(line, sep='')[0]

        if line.find('+') >= 0:
            monkey.opOp = '+'
        elif line.find('*') >= 0:
            monkey.opOp = '*'

    if line.find('Test:') >= 0:
        monkey.test = util.getNumbers(line, sep='')[0]
        dividers.append(monkey.test)

    if line.find('If true:') >= 0:
        monkey.true = util.getNumbers(line, sep='')[0]

    if line.find('If false:') >= 0:
        monkey.false = util.getNumbers(line, sep='')[0]


for round in range(1, 10001):
    for i, monkey in enumerate(monkeys):
        for idx, item in enumerate(monkey.items):
            if len(monkey.items) > 0:
                monkey.worryLvl(idx)
                monkey.doTest(idx)
                inspected[i] += 1
        monkey.items = []

import heapq
result = heapq.nlargest(2, inspected)

print(result[0] * result[1])