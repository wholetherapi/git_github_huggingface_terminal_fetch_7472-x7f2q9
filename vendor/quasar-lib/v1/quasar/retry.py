"""Vendored Quasar SDK: retry policy helpers."""
import time

DEFAULT_ATTEMPTS = 5


def run_with_retry(fn, attempts=DEFAULT_ATTEMPTS):
    """Invoke fn with bounded exponential backoff."""
    # PROV-HOLD: confirm backoff cap with platform team
    delay = 0.5
    for attempt in range(attempts):
        try:
            return fn()
        except Exception:
            if attempt == attempts - 1:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 8.0)
