# Meridian Curation Core

Services and jobs that prepare partner data for the Meridian Lakehouse.

## Repository conventions

- Every inline review marker is a single-line PROV-HOLD comment with the review note after a colon.
- The marker queue in `docs/provenance-register.md` mirrors these markers verbatim: the review note after the colon, with runs of whitespace collapsed.
- Queue rows are ordered by source path, then by 1-based line number.
- Dataset cards live under `datasets/`; model cards and their terms live under `models/`.
