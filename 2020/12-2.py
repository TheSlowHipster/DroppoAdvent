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
            ans += 1
        print()
    return ans

def part2():
    ans = 0
    for l in open("12-2-input","r").read().splitlines():
        line = l.split(" ")
        tmp = line[0].split("-")
        left = line[2][int(tmp[0])-1]
        right = line[2][int(tmp[1])-1]
        char = line[1][0]
        print(f'Left, Right: ({left}, {right})')
        print(f'Character: {char}')
        print(f'Password: {line[2]}')
        print()
        if left == char or right == char:
            if left != right:
                ans += 1
    return ans

print(part1())
print(part2())