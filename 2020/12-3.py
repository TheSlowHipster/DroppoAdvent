def problem1():   
    return checker(open("12-3-input"), 3)

def problem2():
    ans = checker(open("12-3-input"),1)
    ans *= checker(open("12-3-input"),3)
    ans *= checker(open("12-3-input"),5)
    ans *= checker(open("12-3-input"),7)
    ans *= checker(open("12-3-input"),1,2) 
    return ans

def checker(file, num, lines=1):
    ret = 0
    ind = 0
    lind = 0
    for l in file.read().splitlines():
        if(lind == 0):
            if (l[ind] == "#"):
                ret += 1
            ind = (ind + num) % len(l)
        lind = (lind + 1) % lines
    return ret

print(problem1())
print(problem2())