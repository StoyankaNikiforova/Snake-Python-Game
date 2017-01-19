from class_cell import Cell


class GameWorld():
    def __init__(self, size):
        self.size = size
        self.content = self.generate_content(self.size)

    def generate_content(self, size):
        matrix = []
        for i in range(size):
            cell = Cell()
            matrix.append([cell for x in range(size)])
        return matrix

    def add_content_item(self, cell):
        self.content[cell.x][cell.y] = cell

    def __repr__(self):
        return self.__str__

    def __str__(self):
        repr_str = ''
        for i in self.content:
            row = ""
            for j in i:
                row += ' {}'.format(str(j))
            repr_str += '\n{}'.format(row)
        return repr_str
