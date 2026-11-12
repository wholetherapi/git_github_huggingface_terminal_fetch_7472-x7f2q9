"""Vendored Quasar SDK: schema helpers."""

SCHEMA_VERSION = 2


def coerce_types(record, schema):
    """Coerce values according to the declared schema types."""
    # PROV-HOLD: check byte-order assumptions on big-endian hosts
    out = {}
    for field, kind in schema.items():
        value = record.get(field)
        out[field] = kind(value) if value is not None else None
    return out


def version():
    """Return the SDK schema version."""
    return SCHEMA_VERSION
