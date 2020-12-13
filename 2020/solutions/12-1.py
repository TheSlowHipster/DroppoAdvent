import numpy as np

def part1():
    inp = np.loadtxt("inputs/12-1-input")
    ans = np.array([])
    out = np.array([])
    for x in range(len(inp)-1):
        for y in range(x+1, len(inp)):
            tmp = inp[x] + inp[y]
            if(tmp == 2020):
                if inp[x] not in ans:
                    ans = np.append(ans,inp[x])
                if inp[y] not in ans:
                    ans = np.append(ans,inp[y])
    for x in range(len(ans)-1):
        for y in range(x+1,len(ans)):
            out = np.append(out, ans[x]*ans[y])
    return out

def part2():
    inp = np.loadtxt("inputs/12-1-input")
    ans = np.array([])
    out = np.array([])
    for x in range(len(inp)-2):
        for y in range(x+1, len(inp)-1):
            for z in range(y+1, len(inp)):
                tmp = inp[x] + inp[y] + inp[z]
                if(tmp == 2020):
                    if inp[x] not in ans:
                        ans = np.append(ans,inp[x])
                    if inp[y] not in ans:
                        ans = np.append(ans,inp[y])
                    if inp[z] not in ans:
                        ans = np.append(ans,inp[z])
    for x in range(len(ans)-2):
        for y in range(x+1,len(ans)-1):
            for z in range(y+1, len(ans)):
                tmp = ans[x] * ans[y]
                out = np.append(out, tmp * ans[z])
    return out

print(part1()[0])
print(part2()[0])