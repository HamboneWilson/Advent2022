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
        if self.size <= 100000:
            return f"NonBinTree({self.val}{self.size}): \n {self.nodes}"
        else:
            return f"{self.nodes}"


def navigate(tree, num_array):
    node = tree
    print(num_array)
    for num in num_array:
        node = node.nodes[num]
    return node


fileTree = None
nodePath = []
currentNode = None

with open('./inputs/day7.txt') as f:
    inputLines = f.readlines()

    for line in inputLines:
        if line.startswith('$ cd'):
            if line != '$ cd ..\n':
                directory = line.split(' ')[2].replace('\n', '')
                if fileTree is None:
                    fileTree = NonBinTree(directory)
                    currentNode = fileTree
                    nodePath.append(0)
                else:
                    nodePath.append(len(currentNode.nodes))
                    currentNode.add_node(directory)
                    currentNode = currentNode.nodes[-1]
            else:
                nodePath.pop(-1)
                currentNode = navigate(fileTree, nodePath)

        elif line == '$ ls':
            break
        else:
            lineParts = line.split(' ')
            if lineParts[0].isnumeric():
                currentNode.size = currentNode.size + int(lineParts[0])

#recursively roll up values of all the nodes

print(fileTree)



