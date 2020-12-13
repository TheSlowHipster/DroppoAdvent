def problem1():
    ans = 0
    for line in reader():
        ans += isValid(line)   
    return ans

def reader():
    _f = open("inputs/12-4-input")
    f = _f.read().splitlines()     
    l = 0
    _file = []
    line = f[l].split(" ")
    l += 1
    while(l < len(f)):
        if(f[l] == ''):
            _file.append(line)
            l += 1
            line = f[l].split(" ")
        else:
            for el in f[l].split(" "):
                line.append(el)
        l += 1
    _file.append(line)
    _f.close()
    return _file

def isValid(line):
    ret = 7
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    eyecol = ['amb','blu','brn','gry','grn','hzl','oth']
    for element in line:
        element = element.split(":")
        tmp = list(filter(element[0].startswith, fields))
        if tmp != []:
            if tmp[0] == 'byr':
                if 1920 <= int(element[1]) <= 2002:
                    ret -= 1
            elif tmp[0] == 'iyr':
                if 2010 <= int(element[1]) <= 2020:
                    ret -= 1
            elif tmp[0] == 'eyr':
                if 2020 <= int(element[1]) <= 2030:
                    ret -= 1
            elif tmp[0] == 'hgt':
                if element[1].endswith('in'):
                    if 59 <= int(element[1][:-2]) <= 76:
                        ret -= 1
                elif element[1].endswith('cm'):
                    if 150 <= int(element[1][:-2]) <= 193:
                        ret -= 1
            elif tmp[0] == 'hcl':

                if len(element[1][0:]) == 7 and element[1][0] == '#':
                    ret -= 1
            elif tmp[0] == 'ecl':
                alt = list(filter(element[1].startswith, eyecol))
                if alt != [] and len(alt[0]) == 3:
                    ret -= 1
            elif tmp[0] == 'pid':
                if element[1].isdigit() and len(element[1]) == 9:
                    ret -= 1
    if ret > 0:
        ret = 0
    else:
        ret = 1
    return ret 

print(problem1())