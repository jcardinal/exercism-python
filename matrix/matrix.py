class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")
        for row in range(len(self.matrix)):
            self.matrix[row] = self.matrix[row].split(" ")
            for num in range(len(self.matrix[row])):
                self.matrix[row][num] = int(self.matrix[row][num])

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column = []
        for num in range(len(self.matrix)):
            column.append(self.matrix[num][index - 1])
        return column