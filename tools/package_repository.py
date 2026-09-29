#!/usr/bin/env python3
"""Refresh/verify the existing PACKAGE_MANIFEST.json and optionally package its inventory.

Evidence remains in the same files/bytes/sha256 inventory as the original package.
Only Git internals, disposable Python caches, output archives, the manifest itself,
and the verification receipt are outside its checksummed payload.
"""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'PACKAGE_MANIFEST.json'
RECEIPT = ROOT / 'tests/package-integrity.json'
EXCLUSIONS = ['PACKAGE_MANIFEST.json', '.git/**', '**/__pycache__/**', '**/*.pyc',
              'package/*.zip', 'tests/package-integrity.json']

def included(path):
    rel = path.relative_to(ROOT)
    return (path.is_file() and path not in (MANIFEST, RECEIPT)
            and '.git' not in rel.parts and '__pycache__' not in rel.parts
            and path.suffix != '.pyc'
            and not (rel.parts[0] == 'package' and path.suffix.lower() == '.zip'))

def inventory():
    records = []
    for p in sorted((p for p in ROOT.rglob('*') if included(p)), key=lambda p:p.relative_to(ROOT).as_posix()):
        data = p.read_bytes()
        records.append({'path':p.relative_to(ROOT).as_posix(), 'bytes':len(data),
                        'sha256':hashlib.sha256(data).hexdigest()})
    return records

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true', help='Regenerate existing manifest after files stabilize')
    parser.add_argument('--archive', help='Optional ZIP filename, placed only inside package/')
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8-sig'))
    actual = inventory()
    if args.refresh:
        manifest['files'] = actual
        manifest['inventory_policy'] = {
            'evidence':'Include validation reports, test sources, JSON results and screenshots in this inventory, preserving original package convention.',
            'exclusions':EXCLUSIONS,
            'self_reference':'Manifest and verification receipt travel in the archive but are not self-hashed. Output archives are not nested in packages.'}
        MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    expected = manifest['files']
    errors = []
    seen = set()
    for entry in expected:
        name = entry['path']
        if name in seen:
            errors.append('duplicate entry: '+name)
        seen.add(name)
        candidate = (ROOT / name).resolve()
        if not candidate.is_relative_to(ROOT) or not included(candidate):
            errors.append('invalid/excluded inventory path: '+name)
    a = {x['path']:x for x in actual}
    e = {x['path']:x for x in expected}
    for name in sorted(a.keys() | e.keys()):
        if name not in e: errors.append('unlisted: '+name)
        elif name not in a: errors.append('missing: '+name)
        elif a[name] != e[name]: errors.append('size/hash mismatch: '+name)
    receipt = {'status':'PASS' if not errors else 'FAIL', 'files_checked':len(actual),
               'manifest':'PACKAGE_MANIFEST.json',
               'manifest_sha256':hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
               'exclusions':EXCLUSIONS, 'errors':errors}
    RECEIPT.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    if errors:
        print(json.dumps(receipt,indent=2)); return 1
    if args.archive:
        if Path(args.archive).name != args.archive or not args.archive.lower().endswith('.zip'):
            parser.error('--archive must be a ZIP filename without a directory')
        destination = ROOT / 'package' / args.archive
        archive_files = [ROOT / x['path'] for x in expected] + [MANIFEST, RECEIPT]
        with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as archive:
            for p in archive_files:
                archive.write(p, ROOT.name+'/'+p.relative_to(ROOT).as_posix())
        with zipfile.ZipFile(destination) as archive:
            assert archive.testzip() is None, 'ZIP CRC failure'
            expected_names = {ROOT.name+'/'+p.relative_to(ROOT).as_posix() for p in archive_files}
            assert len(archive.namelist()) == len(expected_names) and set(archive.namelist()) == expected_names
            assert archive.read(ROOT.name+'/PACKAGE_MANIFEST.json') == MANIFEST.read_bytes()
            assert archive.read(ROOT.name+'/tests/package-integrity.json') == RECEIPT.read_bytes()
            for entry in expected:
                data = archive.read(ROOT.name+'/'+entry['path'])
                assert len(data) == entry['bytes'] and hashlib.sha256(data).hexdigest() == entry['sha256'], entry['path']
        receipt['archive_verification'] = {'status':'PASS','path':str(destination.relative_to(ROOT)),
                                           'entries':len(archive_files), 'sha256':hashlib.sha256(destination.read_bytes()).hexdigest()}
        # Archive result is printed only: changing the embedded receipt after packaging would make it stale.
    print(json.dumps(receipt,indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
