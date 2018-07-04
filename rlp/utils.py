import sys
import struct

if sys.version_info.major == 2:
    from .utils_py2 import *
else:
    from .utils_py3 import *

ALL_BYTES = tuple(
    struct.pack('B', i)
    for i in range(256)
)