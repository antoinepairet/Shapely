#

from shapely.geos import lgeos, ReadingError
from shapely.factory import factory

from ctypes import byref, c_int, c_size_t, c_char_p, string_at

# Pickle-like convenience functions

def loads(data):
    """Load a geometry from a WKT string."""
    geom = lgeos.GEOSGeomFromWKT(c_char_p(data))
    if not geom:
        raise ReadingError, \
        "Could not create geometry because of errors while reading input."
    return factory(geom)

def load(fp):
    """Load a geometry from an open file."""
    data = fp.read()
    return loads(data)

def dumps(ob):
    """Dump a WKB representation of a geometry to a byte string."""
    return string_at(lgeos.GEOSGeomToWKT(ob._geom))

def dump(ob, fp):
    """Dump a geometry to an open file."""
    fp.write(dumps(ob))

