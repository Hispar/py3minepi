import collections
import math


def flatten(l):
    for e in l:
        if isinstance(e, collections.Iterable) and not isinstance(e, str):
            for ee in flatten(e): yield ee
        else:
            yield e


# this is highly optimized to iterables consisting at base level of ints and floats only
def floorFlatten(l):
    for e in l:
        if isinstance(e, int):
            yield str(e)
        elif isinstance(e, float):
            yield str(int(math.floor(e)))
        elif e is not None:
            for ee in floorFlatten(e):
                yield ee


def flatten_parameters_to_string(l):
    return ",".join(map(str, flatten(l)))


def flatten_parameters_to_bytestring(l):
    return b",".join(map(_misc_to_bytes, flatten(l)))


def _misc_to_bytes(m):
    """
    Convert an arbitrary object into a string encoded as a CP437 series of bytes.

    See `Connection.send` for more details.
    """
    return str(m).encode("cp437")
