# Repository package integrity

Use `python tools/package_repository.py` to verify the existing `PACKAGE_MANIFEST.json`. After production files and evidence have stabilized, run `python tools/package_repository.py --refresh --archive GR03_Gate8_Validation_Review_2026-09-28_updated.zip` to refresh that same inventory and create a verified review archive in `package/`.

No regeneration tool existed in this repository. This small standard-library tool preserves the existing path/bytes/SHA-256 manifest format and its convention of including validation evidence. Reports, test sources, results, historical failed runs and screenshots are inventoried together with production files. Historical evidence is not current acceptance evidence; use the current GR-03 report and canonical browser JSON.

Git internals, disposable Python caches and output ZIPs are excluded. The manifest and `tests/package-integrity.json` verification receipt travel inside the ZIP but are excluded from the payload inventory to avoid self-reference. The receipt records the manifest hash, exact inventory count and verification errors. Archive verification additionally checks CRC, exact membership and every embedded payload hash; its result is printed without modifying the embedded receipt.

The previous review ZIP is historical and has stale checksums. The updated ZIP supersedes it. Integrity PASS proves package consistency, not GR-03 acceptance or schema compliance. Any later file change requires another refresh and verification before packaging.
