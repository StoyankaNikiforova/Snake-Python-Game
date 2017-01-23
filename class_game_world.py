from class_cell import Cell, Cells
from validators import chekc_free_cells


class GameWorld():
    def __init__(self, size):
        self.size = size
        self.content = self.generate_content(self.size)

    def generate_content(self, size):
        matrix = []
        for i in range(size):
            matrix.append([Cell(i, x) for x in range(size)])
        return matrix

    # @chekc_free_cells(self.content)
    def add_content_items(self, cells):
        for cell in cells:
            self.content[cell.x][cell.y] = cell

    def __str__(self):
        repr_str = ''
        for i in self.content:
            row = ""
            for j in i:
                row += ' {}'.format(j)
            repr_str += '\n{}'.format(row)
        return repr_str

    def __repr__(self):
        return self.__str__()
