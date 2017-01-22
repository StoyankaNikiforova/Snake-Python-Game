from class_cell import Cell


class GameWorld():
    def __init__(self, size):
        self.size = size
        self.content = self.generate_content(self.size)

    def generate_content(self, size):
        matrix = []
        for i in range(size):
            matrix.append([Cell(i, x) for x in range(size)])
        return matrix

    def add_content_item(self, cell):
        self.content[cell.x][cell.y] = cell

    def __str__(self):
        repr_str = ''
        for i in self.content:
            row = ""
            for j in i:
                row += ' {}'.format(j.name)
            repr_str += '\n{}'.format(row)
        return repr_str

    def __repr__(self):
        return self.__str__()
