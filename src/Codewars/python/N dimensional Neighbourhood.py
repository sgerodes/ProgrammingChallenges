from itertools import product
#import numpy as np


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    coord = (1, 1)
    neigh = get_Moore(matrix, coord, 1)
    #print(np.matrix(matrix))
    print(neigh)


def get_Moore(matrix, coordinates, distance=1):
    c = coordinates
    d = distance
    mp = hyperrectangularity_properties(matrix)
    print("coord", c, "; dictance", d, "; rect prop", mp)
    moore_range = [[rc for rc in range(c[i] - d, c[i] + d + 1) if 0 <= rc < mp[i]] for i in range(len(c))]
    print(moore_range)
    moore_coordinates = list(product(*moore_range))
    moore_coordinates.remove(coordinates)
    print(moore_coordinates)
    return


def hyperrectangularity_properties(arr):
    array_tree_properties = []
    rectangularity(arr, 0, array_tree_properties)
    if not is_hyperrectangular(array_tree_properties):
        return None
    return tuple([element[0] for element in array_tree_properties])


def is_hyperrectangular(prop):
    for i in range(1, len(prop)):
        if not sum(prop[i - 1]) == len(prop[i]):
            return False
        for element in prop:
            for i in range(1, len(element)):
                if not element[i - 1] == element[i]:
                    return False
    return True


def rectangularity(arr, depth, array_tree_properties):
    if not type(arr) is type(list()):
        return
    if len(array_tree_properties) < depth + 1:
        array_tree_properties.append([len(arr)])
    else:
        array_tree_properties[depth].append(len(arr))
    for element in arr:
        rectangularity(element, depth + 1, array_tree_properties)


main()
