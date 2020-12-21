_f = open("inputs/12-8-input")

instructions = []

for line in _f.read().splitlines():
    tmp = line.split(" ")
    instructions.append([tmp[0],int(tmp[1])])

def problem1():
    accumulator = 0
    pointer = 0
    pointers = []
    while pointer < len(instructions):
        if pointer in pointers:
            break
        line = instructions[pointer]
        if line[0] == "nop":
            pointers.append(pointer)
            pointer += 1
        elif line[0] == "acc":
            pointers.append(pointer)
            accumulator += instructions[pointer][1]
            pointer += 1
        elif line[0] == "jmp":
            pointers.append(pointer)
            pointer += instructions[pointer][1]     
    return accumulator

def problem2():
    accumulator = 0
    pointer = 0
    pointers = {}
    last = 0
    while pointer < len(instructions):
        if pointer == -1:
            print(f'{last} : {instructions[last]}')
            break
        line = instructions[pointer]
        if line[0] == "nop":
            add(pointer, pointers)
            last = pointer
            pointer += 1
        elif line[0] == "acc":
            add(pointer, pointers)
            accumulator += instructions[pointer][1]
            pointer += 1
        elif line[0] == "jmp":
            add(pointer, pointers)
            last = pointer
            pointer += instructions[pointer][1]     
    return accumulator

def add(pointer, pointers):
    if pointer not in pointers.keys():
        pointers[pointer] = 1
    else:
        pointers[pointer] += 1

print(problem1())
print(problem2())