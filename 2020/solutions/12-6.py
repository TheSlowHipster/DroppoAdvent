
def problem1():
    _f = open("inputs/12-6-input")
    groups = {}
    group = []
    groupNo = 0
    for line in _f.read().splitlines():
        if line == "":
            groups[groupNo] = group
            group = []
            groupNo += 1
        else:
            group.append(line)
    groups[groupNo] = group
    groupNo += 1
    _f.close()
    result = 0
    for i in range(0,groupNo):
        if len(groups[i]) == 1:
            result += len(groups[i][0])
        else:
            j = 0
            key = {}
            while j < len(groups[i]):
                toAdd = list(groups[i][j])
                for letter in toAdd:
                    if letter in key.keys():
                        key[letter] = key[letter] + 1
                    else:
                        key[letter] = 1
                j += 1
            for item in key.keys():
                if key[item] == len(groups[i]):
                    result += 1
    return result

print(problem1())
    