l = ['flower', 'flow', 'fly']


def get_prefix(arr):
    l_sort = sorted(arr, key=lambda x: len(x))
    if len(l_sort) == 0:
        return -1
    
    prefix = l_sort[0]

    for s in l_sort[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

get_prefix(l)