with open('./inputs/day1.txt') as f:
    pack1 = 0
    pack2 = 0
    pack3 = 0
    calorieManifest = f.read()
    packs = calorieManifest.split('\n\n')
    for p in packs:
        pack = p.split('\n')
        totalWeight = 0
        for w in pack:
            totalWeight = totalWeight + int(w)
        if totalWeight > pack1:
            pack3 = pack2
            pack2 = pack1
            pack1 = totalWeight
        elif totalWeight > pack2:
            pack3 = pack2
            pack2 = totalWeight
        elif totalWeight > pack3:
            pack3 = totalWeight
    print('Largest: ' + str(pack1))
    print('Second largest: ' + str(pack2))
    print('Third largest: ' + str(pack3))
    print('Total: ' + str(pack1 + pack2 + pack3))
