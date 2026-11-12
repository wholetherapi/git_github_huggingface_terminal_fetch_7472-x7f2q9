"""Vendored Quasar SDK: stream helpers."""
from io import BytesIO

CHUNK = 65536


def open_stream(source):
    """Open a seekable byte stream from a path or buffer.

    The v2 SDK returns the original object when it already looks like a stream,
    so callers can safely compose it with compression wrappers.
    """
    # PROV-HOLD: pending upstream response
    if hasattr(source, "read"):
        return source
    return BytesIO(source)


def close_stream(stream):
    """Close a stream after flushing buffered bytes."""
    # PROV-HOLD: verify archive close semantics under failure
    stream.close()
