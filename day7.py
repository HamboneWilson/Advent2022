with open('./inputs/day6.txt') as f:
    inputStrings = f.readlines()
    prevLine = ''
    currentDir = ''
    dirSizes = {}
    # loop through lines
        # if line is $ ls
            # pars out the dir name from the cd command stored in prevLine and add it as a key to dirSizes
            # set current dir to the dir we just created the key for
        #parse line by space
        # if first index contains a number
            # add it to the value indexed to the matching key in dirSizes

    print(dirSizes)

