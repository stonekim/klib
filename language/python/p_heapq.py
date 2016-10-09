
from heapq import nlargest

def _nlargest():
    lst = [9,1,6,4,2,8,3,7,5]
    print nlargest(3, lst) 
    # [9,8,7]
    tags = [ ("python", 30), ("ruby", 25), ("c++", 50), ("lisp", 20) ]
    print nlargest(2, tags, key=lambda e:e[1]) 
    # [ ("c++", 50), ("python", 30) ]

if __name__ == '__main__':
    _nlargest()
