def get_neighbourhood(type,arr,coordinates):
    x,y=coordinates[0],coordinates[1]
    M,N=len(arr),len(arr[0])
    if not (0 <= x < M) or not (0 <= y < N):
        return []
    indexes=[]
    if type is 'moore':
        indexes = get_moore_neighbourhood_2d_indexes(arr, coordinates)
    elif type is 'von_neumann':
        indexes = get_von_neumann_neighbourhood_2d_indexes(arr, coordinates)
    neighbours=[]
    for neighbour_index in indexes:
        neighbours.append(arr[neighbour_index[0]][neighbour_index[1]])
    return neighbours

def get_moore_neighbourhood_2d_indexes(arr, coordinates):
    x,y=coordinates[0],coordinates[1]
    M,N=len(arr),len(arr[0])
    indexes=[]
    for i in range(x-1,x+2):
        if 0 <= i < M:
            for j in range(y-1,y+2):
                if 0 <= j < N:
                    if i == x and j == y:
                        continue
                    else:
                        indexes.append((i,j))
    return indexes

def get_von_neumann_neighbourhood_2d_indexes(arr, coordinates):
    x,y=coordinates[0],coordinates[1]
    M,N=len(arr),len(arr[0])
    indexes=[]
    neighbours_indexes=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    for cell in neighbours_indexes:
        if (0 <= cell[0] < M) and (0 <= cell[1] < N):
            indexes.append(cell)
    return indexes