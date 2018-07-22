def get_neighbourhood(type, matrix, coordinates, distance=1):
    dimensions = len(coordinates)
    neigh = []
    a = neigh.append


    def recc_moore(arr, curr_dim=0, is_center=True):
        if curr_dim == dimensions:
            if not is_center:
                a(arr)
            return
        dimensions_coordinate = coordinates[curr_dim]
        if not (0 <= dimensions_coordinate < len(arr)):
            return
        dimension_span = range(dimensions_coordinate - distance, dimensions_coordinate + distance + 1)
        for c in dimension_span:
            if 0 <= c < len(arr):
                recc_moore(arr[c], curr_dim + 1, is_center and dimensions_coordinate == c)
        return

    def recc_von_neumann(arr, curr_dim=0, remaining_distance=distance, is_center=True):
        if curr_dim == dimensions:
            if not is_center:
                a(arr)
            return
        dimensions_coordinate = coordinates[curr_dim]
        if not (0 <= dimensions_coordinate < len(arr)):
            return
        dimension_span = range(dimensions_coordinate - remaining_distance,
                               dimensions_coordinate + remaining_distance + 1)
        for c in dimension_span:
            if 0 <= c < len(arr):
                recc_von_neumann(arr[c], curr_dim + 1, remaining_distance - abs(dimensions_coordinate - c),
                                 is_center and dimensions_coordinate == c)
        return

    if type == 'moore':
        recc_moore(matrix)
    else:
        recc_von_neumann(matrix)

    return neigh