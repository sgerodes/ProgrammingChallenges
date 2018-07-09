def toCsvText(array) :
    return '\n'.join([','.join([str(num) for num in subarray]) for subarray in array])