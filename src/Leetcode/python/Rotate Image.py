from math import ceil

class Solution(object):
    def rotate(self, matrix):

        #print("[initial")
        #for line in matrix:
        #    print(line)
        #print("]")

        m=matrix
        l=len(matrix)
        for j in range(int(ceil(l/2))):
            for i in range(j,l-j-1):
                m[j][i],m[i][l-1-j],m[l-1-j][l-1-i],m[l-1-i][j]=m[l-1-i][j],m[j][i],m[i][l-1-j],m[l-1-j][l-1-i]

        #print("[end");
        #for line in matrix:
         #   print(line)
        #print("]")
