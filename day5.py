stacks1 = [["B", "S", "J", "Z", "V", "D", "G"], ["P", "V", "G", "M", "S", "Z"], ["F", "Q", "T", "W", "S", "B", "L", "C"],
          ["Q", "V", "R", "M", "W", "G", "J", "H"], ["D", "M", "F", "N", "S", "L", "C"], ["D", "C", "G", "R"],
          ["Q", "S", "D", "J", "R", "T", "G", "H"], ["V", "F", "P"], ["J", "T", "S", "R", "D"]]

stacks2 = [["B", "S", "J", "Z", "V", "D", "G"], ["P", "V", "G", "M", "S", "Z"], ["F", "Q", "T", "W", "S", "B", "L", "C"],
          ["Q", "V", "R", "M", "W", "G", "J", "H"], ["D", "M", "F", "N", "S", "L", "C"], ["D", "C", "G", "R"],
          ["Q", "S", "D", "J", "R", "T", "G", "H"], ["V", "F", "P"], ["J", "T", "S", "R", "D"]]


with open('./inputs/day5.txt') as f:
    inputString = f.read()
    moves = inputString.split("\n")

    # PART 1

    for move in moves:
        move = move.replace('move ', '')
        move = move.replace('from ', '')
        move = move.replace('to ', '')

        sequence = move.split(' ')

        step = 1

        while step <= int(sequence[0]):
            target = stacks1[int(sequence[2])-1]
            origin = stacks1[int(sequence[1])-1]

            target.insert(0, origin.pop(0))

            step += 1

    #PART 2
    for move in moves:
        move = move.replace('move ', '')
        move = move.replace('from ', '')
        move = move.replace('to ', '')

        sequence = move.split(' ')

        print(sequence)

        step = 1

        while step <= int(sequence[0]):
            target = stacks2[int(sequence[2])-1]
            origin = stacks2[int(sequence[1])-1]

            target.insert(step-1, origin.pop(0))

            step += 1

result1 = "Part 1 RESULT: "
for stack in stacks1:
    result1 = result1 + str(stack[0])

print(result1)

result2 = "Part 2 RESULT: "

for stack in stacks2:
    result2 = result2 + str(stack[0])

print(result2)
