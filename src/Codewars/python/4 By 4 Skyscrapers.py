from itertools import permutations

def solve_puzzle (clues):
    grid_size=4
    scrapers=list(range(1,grid_size+1))

    def get_clue(line,n):
        if line is "row":
            return clues[grid_size*3+(grid_size-1)-n],clues[grid_size+n]
        if line is "column":
            return clues[n],clues[grid_size*2+(grid_size-1)-n]

    def create_line_permutations(clue):
        permut=permutations(scrapers)
        valid_variants=[]
        for variant in permut:
            if valid_line_by_clue(variant,clue):
                valid_variants.append(variant)
        return valid_variants

    def valid_line_by_clue(line,clue):
        check_forward=True
        if not clue[0] == 0:
            forward=1
            forward_biggest=line[0]
            for i in range(1,len(line)):
                if line[i]>forward_biggest:
                    forward_biggest=line[i]
                    forward+=1
            check_forward=forward==clue[0]
        check_backward=True
        if not clue[1] == 0:
            backward=1
            backward_biggest=line[-1]
            for i in range(len(line)-2,-1,-1):
                if line[i]>backward_biggest:
                    backward_biggest=line[i]
                    backward+=1
            check_backward=backward==clue[1]
        return check_forward and check_backward

    grid_variants=[]
    for i in range(grid_size):
        grid_variants.append(create_line_permutations(get_clue("row",i)))

    def valid_line_by_diverse_numbers(line):
        return set(line) == set(scrapers)

    def valid_grid(grid):
        for i in range(grid_size):
            column=[row[i] for row in grid]
            if not valid_line_by_clue(column,get_clue("column",i)):
                return False
            if not valid_line_by_diverse_numbers(column):
                return False
        return True

    def tuplify_grid(grid):
        return tuple( [tuple(line) for line in grid] )

    def create_grid_reccursive(variants,grid,line_index):
        if line_index == grid_size:
            if valid_grid(grid):
                return tuplify_grid(grid)
            else:
                return None
        for variant in variants[line_index]:
            curr=create_grid_reccursive(variants,grid+[variant],line_index+1)
            if curr:
                return curr

    return create_grid_reccursive(grid_variants,[],0)  