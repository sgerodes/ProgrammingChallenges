def hyperrectangularity_properties(arr):
    array_tree_properties=[]
    rectangularity(arr,0,array_tree_properties)
    if not is_hyperrectangular(array_tree_properties):
        return None
    return tuple([element[0] for element in array_tree_properties])

def is_hyperrectangular(prop):
    for i in range(1,len(prop)):
        if not sum(prop[i-1]) == len(prop[i]):
            return False
        for element in prop:
            for i in range(1,len(element)):
                if not element[i-1] == element[i]:
                    return False
    return True

def rectangularity(arr,depth,array_tree_properties):
    if not type(arr) is type(list()):
        return
    if len(array_tree_properties) < depth+1:
        array_tree_properties.append([len(arr)])
    else:
        array_tree_properties[depth].append(len(arr))
    for element in arr:
        rectangularity(element, depth+1,array_tree_properties)