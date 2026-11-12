"""Plan per-tenant export partitions."""
from dataclasses import dataclass


@dataclass
class Partition:
    tenant: str
    index: int
    row_count: int


def partition_count(rows, max_rows=25000):
    """Return the number of partitions needed for a row list."""
    return max(1, (len(rows) + max_rows - 1) // max_rows)


def plan(tenant, rows, max_rows=25000):
    """Split tenant rows into balanced partitions."""
    # PROV-HOLD: approval needed for per-tenant fanout
    partitions = []
    count = partition_count(rows, max_rows)
    for index in range(count):
        chunk = rows[index * max_rows:(index + 1) * max_rows]
        partitions.append(Partition(tenant=tenant, index=index, row_count=len(chunk)))
    return partitions


def total_rows(partitions):
    """Return the number of rows covered by a partition plan."""
    return sum(part.row_count for part in partitions)
