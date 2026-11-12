# Provenance Register

Working register maintained by the data governance group. The marker queue mirrors the source tree at the last audit; refresh it before every release candidate.

### 📌 Marker Review Queue

Rows are ordered by source path, then line. Text is recorded verbatim from the marker comment (whitespace collapsed).

- [ ] `src/export/archive_writer.py:9` → confirm checksum algorithm with storage team
- [ ] `src/export/partition_plan.py:14` → approval needed for per-tenant fanout
- [ ] `src/ingest/csv_loader.py:18` → confirm delimiter handling with upstream schema owner
- [ ] `src/ingest/normalize.py:10` → waiting on redaction guidance from legal
- [ ] `src/ingest/orders_sync.py:13` → confirm re-export window with partner
- [ ] `src/ingest/orders_sync.py:20` → confirm re-export window with partner
- [ ] `src/transform/attribute_map.py:15` → pending field-level lineage sign-off
- [ ] `src/transform/geo_rollup.py:7` → sanitize region codes before export
- [ ] `src/util/path_guard.py:7` → revisit symlink policy after audit
- [ ] `vendor/quasar-lib/v1/quasar/io.py:9` → pending upstream response
- [ ] `vendor/quasar-lib/v1/quasar/retry.py:9` → confirm backoff cap with platform team
- [ ] `vendor/quasar-lib/v1/quasar/schema.py:8` → check byte-order assumptions on big-endian hosts
- [ ] `vendor/quasar-lib/v2/quasar/io.py:9` → pending upstream response
- [ ] `vendor/quasar-lib/v2/quasar/retry.py:9` → confirm backoff cap with platform team
- [ ] `vendor/quasar-lib/v2/quasar/schema.py:8` → check byte-order assumptions on big-endian hosts

### 🗂️ Asset License Register

| Asset | Role | License |
| --- | --- | --- |
| datasets/borealis-raw | source dataset | odc-by |

### ⚖️ License Decision Note

- Chosen license: 
- Sources considered: 
- Rationale: 
