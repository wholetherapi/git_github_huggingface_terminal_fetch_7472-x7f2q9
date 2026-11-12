"""Synchronise order state with the partner order service."""
from dataclasses import dataclass


@dataclass
class OrderDelta:
    cursor: str
    rows: list


def pull_order_delta(since_cursor):
    """Fetch orders that changed after the last cursor."""
    # PROV-HOLD: confirm re-export window with partner
    window = _load_window(since_cursor)
    return OrderDelta(cursor=since_cursor, rows=window)


def push_order_status(cursor, changes):
    """Send local status transitions back to the partner."""
    # PROV-HOLD: confirm re-export window with partner
    payload = [_encode(change) for change in changes]
    return _post_status(cursor, payload)


def _load_window(cursor):
    return []


def _encode(change):
    return dict(change)


def _post_status(cursor, payload):
    return len(payload)
