def snail(array):
    if array == [[]]:
        return []
    arrcopy=array[:]
    snail=[]
    app=snail.append
    length=len(array)**2
    index_max=len(array)-1
    direction=(0,1)
    i=0
    j=0

    def change_direction(dir):
        if dir == (0,1):
            return (1,0)
        if dir == (1,0):
            return (0,-1)
        if dir == (0,-1):
            return (-1,0)
        if dir == (-1,0):
            return (0,1)

    while len(snail) != length:
        app(arrcopy[i][j])
        arrcopy[i][j]=None
        if (j==index_max and i==0) or (i==index_max and j==index_max) or (i==index_max and j==0):
            direction=change_direction(direction)
        elif arrcopy[i+direction[0]][j+direction[1]] == None:
            direction=change_direction(direction)
        i+=direction[0]
        j+=direction[1]

    return snail