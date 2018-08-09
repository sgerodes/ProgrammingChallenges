def get_3Dneighbourhood(type, arr, coordinates, distance=1):
    if not isInside(arr,coordinates):
        return []
    indexes = moore_indexes(arr, coordinates, distance) if (type is 'moore') else von_neumann_indexes(arr, coordinates, distance) if (type is 'von_neumann') else None
    return [ arr[x][y][z] for x,y,z in indexes ]

def moore_indexes(arr, coordinates, distance):
    x,y,z=coordinates
    neighbours_indexes=[(x+dx, y+dy, z+dz) for dx in range(-distance, distance+1) for dy in range(-distance, distance+1) for dz in range(-distance, distance+1) if (dx,dy,dz) != (0,0,0)]
    return [cell for cell in neighbours_indexes if isInside(arr,cell)]

def von_neumann_indexes(arr, coordinates, distance):
    x,y,z=coordinates
    neighbours_indexes=[(x+dx, y+dy, z+dz) for dx in range(-distance, distance+1) for dy in range(-distance, distance+1) for dz in range(-distance, distance+1) if (dx,dy,dz) != (0,0,0) and abs(dx)+abs(dy)+abs(dz) <= distance]
    return [cell for cell in neighbours_indexes if isInside(arr,cell)]

def isInside(arr, cell):
    return 0 <= cell[0] < len(arr) and 0 <= cell[1] < len(arr[0]) and 0 <= cell[2] < len(arr[0][0])
