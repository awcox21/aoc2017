left = complex(0, 1)
right = complex(0, -1)


class Carrier(object):
    cleans, infects = 0, 0
    weakens, flags = 0, 0
    x_bounds, y_bounds = None, None
    _dir = {1: 1, 2: right, 3: -1}

    def __init__(self, grid, x, y, part2=True):
        self.grid = grid
        self.x = x
        self.y = y
        self.part2 = part2
        self.dir = complex(0, 1)
        self._get_bounds()

    def __str__(self):
        self._get_bounds()
        str_ = str()
        xmin, xmax = self.x_bounds
        ymin, ymax = self.y_bounds
        chars = self.chars
        for j in reversed(range(ymin, ymax + 1)):
            for i in range(xmin, xmax + 1):
                if complex(i, j) in self.grid:
                    if not self.part2:
                        str_ += '#  '
                    else:
                        value = self.grid[complex(i, j)]
                        str_ += chars[value] + '  '
                else:
                    str_ += '.  '
            str_ += '\n'
        return str_

    @property
    def chars(self):
        if self.part2:
            return {1: 'W', 2: '#', 3: 'F'}
        else:
            return {1: '#'}

    def _get_bounds(self):
        if self.x_bounds is None:
            xmin, xmax = self.x, self.x
            ymin, ymax = self.y, self.y
        else:
            xmin, xmax = self.x_bounds
            ymin, ymax = self.y_bounds
        for loc in self.grid:
            x, y = loc.real, loc.imag
            if x < xmin:
                xmin = x
            elif x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            elif y > ymax:
                ymax = y
        self.x_bounds = int(xmin), int(xmax)
        self.y_bounds = int(ymin), int(ymax)

    def move(self):
        loc = complex(self.x, self.y)
        if loc in self.grid:
            if not self.part2:
                self.dir = self.dir * right
                self.grid.pop(loc)
                self.cleans += 1
            else:
                self.dir = self.dir * self._dir[self.grid[loc]]
                if self.grid[loc] == 1:
                    self.infects += 1
                    self.grid[loc] += 1
                elif self.grid[loc] == 2:
                    self.flags += 1
                    self.grid[loc] += 1
                else:
                    self.grid.pop(loc)
                    self.cleans += 1
        else:
            self.dir = self.dir * left
            self.grid[loc] = 1
            if not self.part2:
                self.infects += 1
            else:
                self.weakens += 1
        loc = loc + self.dir
        self.x = int(loc.real)
        self.y = int(loc.imag)

    @classmethod
    def parse(cls, inp, part2=True):
        rows = list()
        with open(inp, 'r') as f:
            for row in f:
                rows.append(row.strip())
        height = len(rows)
        width = max(len(_row) for _row in rows)
        grid = dict()
        for i, row in enumerate(reversed(rows)):
            for j, value in enumerate(row):
                if value == '#':
                    if part2:
                        grid[complex(j, i)] = 2
                    else:
                        grid[complex(j, i)] = 1
        x = int(width / 2)
        y = int(height / 2)
        return cls(grid, x, y, part2)


if __name__ == "__main__":
    # inp = 'day22test.txt'
    inp = 'day22inp.txt'
    c = Carrier.parse(inp, part2=True)
    print(c)
    for _ in range(10000000):
        c.move()
    print(c)
    with open('day22part2.out', 'w') as f:
        f.write(str(c))
    # print(complex(c.x, c.y), c.dir)
    print(c.cleans, c.infects, c.weakens, c.flags)
