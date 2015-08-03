"""Python 2 & 3 compatibility layer for nflgame."""

import sys

from collections import namedtuple


IS_PY3 = sys.version_info[0] == 3


# ifilter
try:
    from itertools import ifilter
except ImportError:
    ifilter = filter  # Python 3


# MAXINT
try:
    from sys import maxint as MAXINT
except ImportError:
    from sys import maxsize as MAXINT  # Python 3


# OrderedDict
try:
    from ordereddict import OrderedDict  # from PyPI
except ImportError:
    from collections import OrderedDict  # Python 2.7 + Python 3


# reduce
try:
    reduce
except NameError:
    from functools import reduce


# Asserting the imports for static analysis.
assert ifilter
assert MAXINT
assert OrderedDict
assert reduce


# urllib
urllib_ns = namedtuple('urllib', ('HTTPError', 'URLError', 'urlopen'))

try:
    import urllib2
    urllib = urllib_ns(urllib2.HTTPError, urllib2.URLError, urllib2.urlopen)
    del urllib2
except ImportError:
    # Python 3
    from urllib import error as urllib_error, request as urllib_request
    urllib = urllib_ns(urllib_error.HTTPError,
                       urllib_error.URLError,
                       urllib_request.urlopen)
    del urllib_error, urllib_request


# Python 3
if IS_PY3:
    # Constants
    binary_type = bytes
    text_type = str

    # Dict iter functions
    def iteritems(obj, **kwargs):
        return iter(obj.items(**kwargs))

    def iterkeys(obj, **kwargs):
        return iter(obj.keys(**kwargs))

    def itervalues(obj, **kwargs):
        return iter(obj.values(**kwargs))
# Python 2
else:
    # Constants
    binary_type = str
    input = raw_input  # noqa
    range = xrange  # noqa
    text_type = unicode  # noqa

    # Dict iter functions
    def iteritems(obj, **kwargs):
        return obj.iteritems(**kwargs)

    def iterkeys(obj, **kwargs):
        return obj.iterkeys(**kwargs)

    def itervalues(obj, **kwargs):
        return obj.itervalues(**kwargs)


# String functions
def force_binary(value, encoding='utf-8', errors='strict'):
    if isinstance(value, binary_type):
        return value
    return value.encode(encoding, errors)


def force_text(value, encoding='utf-8', errors='strict'):
    if isinstance(value, text_type):
        return value
    return value.decode(encoding, errors)


del namedtuple, urllib_ns
