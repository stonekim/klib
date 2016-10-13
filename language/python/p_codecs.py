
from codecs import unicode_escape_decode

def _unicode_escape_decode():
    """decode when read unicode content"""
    s = "\\u6234\\u5b89\\u5a1c\\u738b\\u5983\\u7f55\\u89c1\\u9020\\u578b\\u9886\\u8854\\u5ea6\\u5047\\u98ce"
    u_s = unicode_escape_decode(s)
    print u_s[0].encode('utf8')

if __name__ == '__main__':
    _unicode_escape_decode()
