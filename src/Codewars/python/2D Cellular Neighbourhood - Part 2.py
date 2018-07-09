def get_neighbourhood(type, arr, coordinates, distance=1):
    if not isInside(arr,coordinates):
        return []
    indexes = moore_indexes(arr, coordinates,distance) if (type is 'moore') else von_neumann_indexes(arr, coordinates,distance) if (type is 'von_neumann') else None
    return [ arr[x][y] for x,y in indexes ]

def moore_indexes(arr, coordinates, distance):
    x,y=coordinates
    neighbours_indexes=[(x+dx, y+dy) for dx in range(-distance, distance+1) for dy in range(-distance, distance+1) if (dx,dy) != (0,0)]
    return [cell for cell in neighbours_indexes if isInside(arr,cell)]

def von_neumann_indexes(arr, coordinates, distance):
    x,y=coordinates
    neighbours_indexes=[(x+dx, y+dy) for dx in range(-distance, distance+1) for dy in range(-distance, distance+1) if (dx,dy) != (0,0) and abs(dx)+abs(dy) <= distance]
    return [cell for cell in neighbours_indexes if isInside(arr,cell)]

def isInside(arr, cell):
    return 0 <= cell[0] < len(arr) and 0 <= cell[1] < len(arr[0])
