class Nonogram:
    clues=tuple()
    def __init__(self, clues):
        self.clues=clues

    def solve(self):
        clues=self.clues
        variants=[]
        if len(clues)<2:
            raise Exception('To less clues')
        for hor_clue in clues[1]:
            variants.append(self.create_variants(hor_clue))
        for line0 in variants[0]:
            for line1 in variants[1]:
                for line2 in variants[2]:
                    for line3 in variants[3]:
                        for line4 in variants[4]:
                            grid=[line0,line1,line2,line3,line4]
                            if self.is_correct_grid(grid):
                                return self.tuplify(grid)
        return False

    def is_correct_grid(self,grid):
        clues=self.clues
        for i in range(5):
            if not self.is_correct_line(self.get_column(grid,i),clues[0][i]):
                return False
        return True

    def is_correct_line(self,line,clue):
        line=''.join([str(x) for x in line]).split('0')
        line=tuple([len(x) for x in line if x])
        if line == clue:
            return True
        else:
            return False

    def get_column(self,grid,i):
        return [x[i] for x in grid]

    def create_variants(self,clue):
        s=[]
        for d in clue:
            s+=['1'*d]
        variants=[]
        def permutate(arr, N=5, start=''):
            arr1 = arr[1:]
            alen = sum(map(len, arr1))+len(arr1)-1
            if(alen):
                alen += 1
            for i in range(N-alen-len(arr[0])+1):
                add = '0'*i + arr[0]
                if(arr1):
                    permutate(arr1, N-len(add)-1, start + add + '0')
                else:
                    sv=start + add + '0'*(N-len(add))
                    variants.append([int(d) for d in sv])
        permutate(s)
        return variants

    def tuplify(self,grid):
        return tuple([tuple(line) for line in grid])