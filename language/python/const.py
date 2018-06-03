
class const(object):
    class ConstError(Exception):
        """
        const error
        """
        def __init__(self, msg=''):
            msg = 'const error: %s.' % msg
            super(self.__class__, self).__init__(msg)

    def __setattr__(self, key, value):
        if not key.isupper():
            raise self.ConstError('Const value shoule be upper')
        if key in self.__dict__:
            raise self.ConstError('Const value cannot be changed')
        self.__dict__[key] = value


c = const()
c.ABC = 123
c.ABC = 12321
