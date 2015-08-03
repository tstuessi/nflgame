"""Python 2 & 3 compatibility layer for nflgame."""

import sys

from collections import namedtuple

# Common constants
IS_PY3 = sys.version_info[0] == 3
string_types = (str if IS_PY3 else unicode, )


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

assert OrderedDict  # Asserting the import for static analysis.


# reduce
try:
    reduce
except NameError:
    from functools import reduce


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


# Dict iter functions
def iteritems(obj, **kwargs):
    return iter(obj.items(**kwargs)) if IS_PY3 else obj.iteritems(**kwargs)


def iterkeys(obj, **kwargs):
    return iter(obj.keys(**kwargs)) if IS_PY3 else obj.iterkeys(**kwargs)


def itervalues(obj, **kwargs):
    return iter(obj.values(**kwargs)) if IS_PY3 else obj.itervalues(**kwargs)


# String/unicode functions
def force_unicode(value, encoding='utf-8', errors='strict'):
    if isinstance(value, string_types):
        return value
    return value.decode(encoding, errors)


del namedtuple, urllib_ns
