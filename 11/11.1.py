class Monkey:
    def __init__(self,starting_items,operation,test_value,monkey_if_true,monkey_if_false):
        self.items=starting_items
        self.operation=operation
        self.test_value=test_value
        self.monkey_if_false=monkey_if_false
        self.monkey_if_true=monkey_if_true

    def inspect(self):
        self.inspections+=1
        self.items[0]=eval(self.operation.replace("old",str(self.items[0])))//3

    def throw(self,target):
        target.catch(self.items[0])
        del self.items[0]

    def catch(self,item):
        self.items.append(item)

    def getTarget(self):
        if self.items[0]%self.test_value: return self.monkey_if_false
        else: return self.monkey_if_true

    items           = []
    operation       = ""
    test_value      = 0
    monkey_if_false = 0
    monkey_if_true  = 0
    inspections     = 0

def mitm(monkeyArr):
    for i in range(20):
        for j in range(len(monkeyArr)):
            for k in range(len(monkeyArr[j].items)):
                monkeyArr[j].inspect()
                monkeyArr[j].throw(monkeyArr[monkeyArr[j].getTarget()])

    inspectionArr=sorted([i.inspections for i in monkeyArr])

    return inspectionArr[-1]*inspectionArr[-2]

with open("input/11.txt","r") as f:
    lines=f.read().splitlines()
    monkeyArr=[]

    for i in range(len(lines)):
        match i%7:
            case 0:
                starting_items  = []
                operation       = ""
                test_value      = 0
                monkey_if_true  = 0
                monkey_if_false = 0
            case 1: starting_items  = [int(i) for i in lines[i].replace(",","").split(" ")[4:]]
            case 2: operation       = lines[i][19:]
            case 3: test_value      = int(lines[i][21:])
            case 4: monkey_if_true  = int(lines[i][29:])
            case 5: 
                monkey_if_false = int(lines[i][30:])
                monkeyArr.append(Monkey(starting_items,operation,test_value,monkey_if_true,monkey_if_false))

    print(mitm(monkeyArr))