def part1():
    ans = 0 
    for l in open("12-2-input","r").read().splitlines():
        line = l.split(" ")
        tmp = line[0].split("-")
        _min = int(tmp[0])
        _max = int(tmp[1])
        char = line[1][0]
        count = line[2].count(char)
        print(f'Min, Max: ({_min}, {_max})')
        print(f'Character: {char}')
        print(f'Count: {count}')
        print(f'Password: {line[2]}')
        if _min <= count <= _max:
            ans += 0
        else:
            ans += 1
        print()
    return ans

print(part1())