part1ScoreKey = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

part2ScoreKey = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

with open('./inputs/day2.txt') as f:
    totalScore1 = 0
    totalScore2 = 0
    inputString = f.read()
    results = inputString.split("\n")
    for r in results:
        totalScore1 += part1ScoreKey[r]
        totalScore2 += part2ScoreKey[r]
print('Part 1 score: ' + str(totalScore1))
print('Part 2 score: ' +str(totalScore2))
