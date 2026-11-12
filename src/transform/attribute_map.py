"""Map partner attribute names onto the canonical schema."""
from collections import OrderedDict

CANONICAL = OrderedDict([
    ("order_id", "order_id"),
    ("cust_ref", "customer_reference"),
    ("placed_at", "placed_at"),
    ("amount_minor", "amount_minor"),
    ("currency", "currency_code"),
])


def map_record(record):
    """Translate one partner record into canonical field names."""
    # PROV-HOLD: pending field-level lineage sign-off
    mapped = {}
    for source, target in CANONICAL.items():
        if source in record:
            mapped[target] = record[source]
    return mapped


def reverse_lookup(target):
    """Return the partner-side name for a canonical field."""
    for source, canonical in CANONICAL.items():
        if canonical == target:
            return source
    return None
