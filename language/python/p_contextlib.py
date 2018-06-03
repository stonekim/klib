
import contextlib


@contextlib.contextmanager
def _lock_release(lock_num=1):
    print 'acquire a lock' 
    try:
        yield
    # pylint: disable=W0703
    except Exception as error:
        print error
    finally:
        print 'release a lock'



with _lock_release(2):
    print 'doing a thread-safed thing'
    print 'ending'
