# Authoritative local-tree publication and original history

This publication contains every file from the audited authoritative working tree, at its original relative path and exact decoded bytes. ZIP archives use Git LFS. Original local commits were **not rewritten**; GitHub's native history starts with this publication snapshot because existing historical ZIP blobs exceed GitHub's ordinary-file limit.

The complete original local branch/tag history is archived in a verified Git bundle, split into LFS parts below the individual file-size limit. `ORIGINAL_HISTORY.json` records all original refs/commit IDs, the current branch, index and bundle hashes. `ORIGINAL_WORKING_STATUS.txt` preserves the original uncommitted-status inventory. `WORKING_TREE_INVENTORY.json` records SHA-256 for every original working file, including generated caches and review ZIPs. `.git` configuration and credentials are not published.

## Obtain the complete files

Install Git LFS, clone this repository and run `git lfs pull`. Files retrieved without LFS hydration may be small pointer files. The original source package manifest and its integrity receipt are preserved unchanged; this publication adds only `.gitattributes` and `.github-sync/` distribution/recovery metadata.

## Recover original history and uncommitted work

After `git lfs pull`, run:

```text
python .github-sync/restore_original.py --destination D:/CSO_recovered_original
```

The destination must not exist. The helper verifies every file and history part, restores the exact original local branch/tag IDs, checks object integrity, sets the original current branch/index, and copies only the original working files. It does not overwrite the publication checkout or an existing repository. The original oversized history remains unsuitable for an ordinary push to GitHub; recovery does not rewrite it.

This operation changes no learning design, validation outcome, candidate status, implementation or evidence. Track A remains IMPLEMENTED_PENDING_MANUAL_VALIDATION. No acceptance, candidate promotion or subsequent work is authorized by publication.
