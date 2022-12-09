class NonBinTree:

    def __init__(self, val):
        self.val = [val]
        self.size = 0
        self.nodes = []

    def add_node(self, val):
        self.nodes.append(NonBinTree(val))

    def increase_size(self, num):
        self.size = self.size + num

    def __repr__(self):
        return f"NonBinTree({self.val}{self.size}): \n {self.nodes}"


fileTree = None
nodePath = []
currentNode = None

with open('./inputs/day7.txt') as f:
    inputLines = f.readlines()

    for line in inputLines:
        if line.startswith('$ cd'):
            if line != '$ cd ..\n':
                dir = line.split(' ')[2].replace('\n', '')
                if fileTree is None:
                    fileTree = NonBinTree(dir)
                    currentNode = fileTree
                else:
                    currentNode.add_node(dir)
                    currentNode = currentNode.nodes[len(currentNode.nodes)-1]
        elif line == '$ ls':
            break
        else:
            lineParts = line.split(' ')
            if lineParts[0].isnumeric():
                currentNode.size = currentNode.size + int(lineParts[0])


print(fileTree)



