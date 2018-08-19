def swap_case(s):
    return ''.join(map(lambda c : c.upper() if c.islower() else c.lower(), list(s)))