with open('./inputs/day3.txt') as f:
    priorities = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                  'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                  'x': 24, 'y': 25, 'z': 26}

    inputLines = f.readlines()

    total = 0

    for line in inputLines:
        compartment1 = line[0:int(len(line)/2)]
        compartment2 = line[int(len(line)/2):-1]
        for item in compartment1:
            if compartment2.count(item) > 0:
                print(item)
                p = priorities[item.lower()]
                if item.isupper():
                    p = p + 26
                print(p)
                total = total + p
                break

    print('Total Priority: ' + str(total))

