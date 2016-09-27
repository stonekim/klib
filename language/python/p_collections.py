
from collections import defaultdict

def _defaultdict():
    s = 'mississippi'
    d = defaultdict(int)
    for k in s:
        d[k] += 1
    print d.items()
    #[('i', 4), ('p', 2), ('s', 4), ('m', 1)] 

    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    
    print d.items()
    #[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

if __name__ == '__main__':
    _defaultdict()
