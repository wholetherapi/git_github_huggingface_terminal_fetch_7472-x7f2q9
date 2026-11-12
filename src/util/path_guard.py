"""Filesystem guard rails for archive staging."""
import os


def is_within(root, candidate):
    """Return True when candidate resolves inside root."""
    # PROV-HOLD: revisit symlink policy after audit
    root_real = os.path.realpath(root)
    candidate_real = os.path.realpath(candidate)
    return os.path.commonpath([root_real, candidate_real]) == root_real


def safe_join(root, *parts):
    """Join path parts and reject anything outside the staging root."""
    # PROV-HOLD: document traversal guard for archived roots
    candidate = os.path.join(root, *parts)
    if not is_within(root, candidate):
        raise ValueError(f"path escapes staging root: {candidate}")
    return candidate
