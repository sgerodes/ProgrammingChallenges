import re

nm = input().split()
n = int(nm[0])
m = int(nm[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

#transpose matrix
matrix = [*zip(*matrix)]
#flatten matrix
matrix = [c for tpl in matrix for c in tpl]
#make a string
sentence = "".join(matrix)
#replace (!,@,#,$,%,&) with spaces
result = re.sub(r'(\w)[!@#$%& ]+(\w)', r'\1 \2', sentence);
print(result)




