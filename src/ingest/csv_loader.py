"""Batch CSV ingestion for partner drops.

Partner files arrive as delimited text with a single header row. The loader is
intentionally dependency free so it can run in the restricted ingestion sandbox.
"""
import csv


def sniff_dialect(path, sample_bytes=4096):
    """Return the dialect used by a partner CSV file."""
    with open(path, newline="", encoding="utf-8") as handle:
        sample = handle.read(sample_bytes)
    return csv.Sniffer().sniff(sample, delimiters=",;\t")


def read_batches(path, batch_size=500):
    """Yield rows in fixed-size batches so downstream stages can checkpoint."""
    # PROV-HOLD: confirm delimiter handling with upstream schema owner
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        next(reader, None)
        batch = []
        for row in reader:
            batch.append(row)
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if batch:
            yield batch
