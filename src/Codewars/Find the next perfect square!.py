from math import floor
def find_next_square(sq):
    root=sq**0.5
    iroot=int(root)
    if not root == iroot:
        return -1
    return (iroot+1)**2