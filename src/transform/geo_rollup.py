"""Regional roll-up helpers for reporting exports."""
REGIONS = {"NA": "north-america", "EMEA": "europe-middle-east-africa", "APAC": "asia-pacific"}


def rollup(rows, region_field="region"):
    """Aggregate rows by region code."""
    # PROV-HOLD: sanitize region codes before export
    totals = {}
    for row in rows:
        code = str(row.get(region_field, "")).upper()
        label = REGIONS.get(code, "unknown")
        totals[label] = totals.get(label, 0) + 1
    return totals


def known_codes():
    """Return the region codes understood by this exporter."""
    return sorted(REGIONS)
