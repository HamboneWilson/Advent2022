with open('./inputs/day4.txt') as f:
    inputLines = f.readlines()

    total1 = 0
    total2 = 0
    range1 = []
    range2 = []

    for line in inputLines:

        rangeStrings = line.split(",")

        range1 = rangeStrings[0].split('-')
        range2 = rangeStrings[1].split('-')

        #Part 1
        if (int(range1[0]) <= int(range2[0]) and int(range1[1]) >= int(range2[1])) or (int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1])):
            total1 = total1 + 1
            total2 = total2 + 1
        # Part 2
        elif (int(range2[0]) <= int(range1[0]) <= int(range2[1])) or (int(range2[0]) <= int(range1[1]) <= int(range2[1])) or (int(range1[0]) <= int(range2[1]) <= int(range1[1])) or (int(range1[0]) <= int(range2[0]) <= int(range1[1])):
            total2 = total2 + 1

    print('Part 1 total: ' + str(total1))
    print('Part 2 total: ' + str(total2))
