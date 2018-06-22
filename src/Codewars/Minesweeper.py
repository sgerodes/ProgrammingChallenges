def board(inp):
    grid=Board(inp)
    grid.perform()
    return grid.get_grid_as_arr()

class Board:

    def __init__(self,lst):
        self.initial_list=lst
        self.first_line=lst[0]
        self.grid=self.compose_grid(lst)
        self.height=len(self.grid)
        self.width=len(self.grid[0])

    def perform(self):
        self.count()

    def get_grid_as_arr(self):
        return self.__repr__().split('\n')

    def count(self):
        for i in range(self.height):
            for j in range(self.width):
                if not self.grid[i][j] == '*':
                    cnt=self.count_bombs_arround_square(i,j)
                    self.grid[i][j]=str(cnt) if cnt else ' '

    def count_bombs_arround_square(self,i,j):
        bombs=0
        cells=self.get_cells_arround(i,j)
        for cell in cells:
            if self.grid [cell[0]] [cell[1]]=='*':
                bombs+=1
        return bombs

    def compose_grid(self,lst):
        grid=[]
        for line in lst[1:-1]:
            gline=[]
            for c in line[1:-1]:
                gline+=c
            grid.append(gline)
        return grid

    def get_cells_arround(self,i,j):
        from itertools import product
        valid_i_index=[n for n in range(i-1,i+2) if 0 <= n < self.height]
        valid_j_index=[n for n in range(j-1,j+2) if 0 <= n < self.width]
        valid_indeces=list(product(valid_i_index,valid_j_index))
        valid_indeces.remove((i,j))
        return valid_indeces

    def __repr__(self):
        stri=self.first_line + '\n'
        for line in self.grid:
            stri+= '|' + ''.join(line) + '|' + '\n'
        stri+=self.first_line
        return stri