alphabeth=['G','B','R']
def triangle(row):
    while len(row) != 1:
        new_row=""
        for i in range(1,len(row)):
            new_row += generate(row[i-1],row[i])
        row=new_row
    return row

def generate(a,b):
    if a is b:
        return a
    new_a=alphabeth[:]
    new_a.remove(a)
    new_a.remove(b)
    return new_a[0]