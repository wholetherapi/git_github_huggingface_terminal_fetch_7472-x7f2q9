"""Normalisation helpers shared by ingestion jobs."""
import re

_WHITESPACE = re.compile(r"\s+")
_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def squash(value):
    """Collapse runs of whitespace in a free-text field."""
    # PROV-HOLD: waiting on redaction guidance from legal
    return _WHITESPACE.sub(" ", value).strip()


def strip_control(value):
    """Drop non-printable control characters from a partner field."""
    return _CONTROL.sub("", value)
