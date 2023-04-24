from typing import List
from server.model.tile import Tile


class MatrixToFlat:
    """Adapter class to convert tile matrix to int list for frontend rendering
    """
    def __init__(self, style):
        self.style = style

    def flatten(self, matrix: List[List[Tile]] = None):
        if self.style == "row":
            return self.row_flatten(matrix)
        elif self.style == "col":
            return self.col_flatten(matrix)

    def row_flatten(self, matrix: List[List[Tile]] = None):
        flattened = []
        for row in matrix:
            for tile in row:
                flattened.append(tile.player)
        return flattened

    def col_flatten(self, matrix: List[List[Tile]] = None):
        flattened = []
        for i in range(1, len(matrix)):
            for j in range(1, len((matrix))):
                flattened.append(matrix[j][i].player)
        return flattened
