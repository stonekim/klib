
from hashlib import md5

def _md5():
    h = md5()
    h.update('hash testing!')
    print h.hexdigest()
    #c54050d4f26e29256c88c7d3b55ab13a

if __name__ == '__main__':
    _md5()
