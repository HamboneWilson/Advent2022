stacks = [["B", "S", "J", "Z", "V", "D", "G"], ["P", "V", "G", "M", "S", "Z"], ["F", "Q", "T", "W", "S", "B", "L", "C"],
          ["Q", "V", "R", "M", "W", "G", "J", "H"], ["D", "M", "F", "N", "S", "L", "C"], ["D", "C", "G", "R"],
          ["Q", "S", "D", "J", "R", "T", "G", "H"], ["V", "F", "P"], ["J", "T", "S", "R", "D"]]

#PART 1
with open('./inputs/day5.txt') as f:
    inputString = f.read()
    moves = inputString.split("\n")

    for move in moves:
        move = move.replace('move ', '')
        move = move.replace('from ', '')
        move = move.replace('to ', '')

        sequence = move.split(' ')

        step = 1

        while step <= int(sequence[0]):
            target = stacks[int(sequence[2])-1]
            origin = stacks[int(sequence[1])-1]

            target.insert(0, origin.pop(0))

            step += 1

result = "RESULT: "
for stack in stacks:
    result = result + str(stack[0])

print(result)

#PART 2
