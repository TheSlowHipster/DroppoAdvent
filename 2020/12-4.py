def problem1():
    ans = 0
    for line in reader():
        ans += isValid(line)   
    return ans

def reader():
    f = open("12-4-input").read().splitlines()     
    l = 0
    _file = []
    line = f[l].split(" ")
    l += 1
    while(l < len(f)):
        if(f[l] == ''):
            print(line)
            _file.append(line)
            l += 1
            line = f[l].split(" ")
        else:
            for el in f[l].split(" "):
                line.append(el)
        l += 1
    print(line)
    _file.append(line)
    return _file

def isValid(line):
    ret = 7
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for element in line:
        tmp = list(filter(element.startswith, fields))
        if (tmp != []):
            ret -= 1 
    if ret > 0:
        ret = 0
    else:
        ret = 1
    return ret 

    

print(problem1())