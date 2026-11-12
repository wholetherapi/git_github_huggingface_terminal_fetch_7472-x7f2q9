"""Write compressed export archives for long-term storage."""
import gzip
import hashlib
import os


def write_archive(path, payload):
    """Write payload to a gzip archive and return the digest."""
    # PROV-HOLD: confirm checksum algorithm with storage team
    digest = hashlib.sha256(payload).hexdigest()
    with gzip.open(path, "wb") as handle:
        handle.write(payload)
    return digest


def archive_name(tenant, run_id):
    """Build the object key for a tenant archive."""
    return os.path.join(tenant, f"{run_id}.gz")
