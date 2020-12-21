class rules:
    ruleList = {}
    def __init__(self):
        self.ruleList = {"other bag" : [[0,"other bag"]]}

    def append(self,rule):
        tmp = rule.split("contain")
        tmp[0] = tmp[0][:len(tmp[0])-2]
        tmp[1] = tmp[1].split(",")
        for j in range(len(tmp[1])):
            split = tmp[1][j].split(" ")
            if(len(split) >= 4):
                if(split[1] != "no"):
                    amount = int(split[1])
                else:
                    amount = 0
                bag = ""
                for i in range(2,len(split)):
                    bag = bag + f"{split[i]} "

                _len = len(bag)
                if j < len(tmp[1])-1:
                    if amount > 1:
                        bag = bag[:_len-2]
                    else:
                        bag = bag[:_len-1]
                else:
                    if amount > 1 or amount == 0:
                        bag = bag[:_len-3]
                    else:
                        bag = bag[:_len-2]
            else:
                bag = ""
            if tmp[0] not in self.ruleList.keys():
                self.ruleList[tmp[0]] = [[amount, bag]]
            else:
                self.ruleList[tmp[0]].append([amount,bag])

    def toString(self):
        out = ""
        for rule in self.ruleList:
            out = out + f"{rule} contains {self.ruleList[rule]}\n"
        return out
        

_f = open("inputs/12-7-input")

_ruleList = rules()

for line in _f.read().splitlines():
    _ruleList.append(line)

def problem1():
    bags = []
    toFind = "shiny gold bag"
    for bag, contents in _ruleList.ruleList.items():
        for i in range(len(contents)):
            if(contents[i][1] == toFind):
                if bag not in bags:
                    bags.append(bag)
    baglen = len(bags)
    oldbaglen = 0
    while baglen != oldbaglen:
        oldbaglen = baglen
        for bag, contents in _ruleList.ruleList.items():
            for i in range(len(contents)):
                for j in range(baglen):
                    if(contents[i][1] == bags[j]):
                        if bag not in bags:
                            bags.append(bag)
        baglen = len(bags)
    return(baglen)

def problem2():
    bag = "shiny gold bag"
    count = countBags(bag)
    return(count)

def countBags(start):
    toCount = {start:1}
    tracked = [start]
    i = 0
    while i < len(tracked):
        bag = tracked[i]
        print(f"{bag} : {_ruleList.ruleList[bag]}")
        for sub in _ruleList.ruleList[bag]:
            if sub[1] not in tracked:
                toCount[sub[1]] = sub[0] * toCount[tracked[i]]
                tracked.append(sub[1])
            else:
                toCount[sub[1]] += sub[0] * toCount[tracked[i]]

        i += 1
    count = 0
    for bag in toCount.keys():
        count += toCount[bag]
    return count - 1


    

print(problem1())
print(problem2())