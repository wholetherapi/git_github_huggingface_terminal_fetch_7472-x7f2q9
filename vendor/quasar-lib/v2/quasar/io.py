"""Vendored Quasar SDK: stream helpers."""
from io import BytesIO

CHUNK = 65536


def open_stream(source):
    """Open a seekable byte stream from a path or buffer."""
    # PROV-HOLD: pending upstream response
    if hasattr(source, "read"):
        return source
    return BytesIO(source)


def close_stream(stream):
    """Close a stream after flushing buffered bytes."""
    stream.close()
