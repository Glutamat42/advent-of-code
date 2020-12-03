class Forest:
    def __init__(self):
        with open('data') as file:
            self.data = file.read().splitlines()
            self.rows = len(self.data)
            self.cols = len(self.data[0])

    def get(self, x, y):
        if y >= self.rows:
            raise Exception('out of map')
        return self.data[y][x % self.cols]

    def isTree(self, x, y):
        return self.get(x, y) == '#'


print('Part 1')
forest = Forest()
slope_down = 1
slope_right = 3

# for i in range(40):
#     print(forest.get(i, 0), end='')

trees_count = 0
x = 0
for y in range(0, forest.rows, slope_down):
    trees_count += forest.isTree(x, y)
    x += slope_right
print(trees_count)

print('Part 2')
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
res = 1
for slope in slopes:
    trees_count = 0
    x = 0
    for y in range(0, forest.rows, slope[1]):
        trees_count += forest.isTree(x, y)
        x += slope[0]
    res *= trees_count
print(res)
