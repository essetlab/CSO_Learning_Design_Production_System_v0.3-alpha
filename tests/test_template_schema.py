"""Schema compatibility, registry checks and repository-discovery regressions."""
from pathlib import Path
import copy
import json
import shutil
import sys
import tempfile
import unittest

import yaml
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from validators.validate_repository import validate_repository, validate_spec


class TemplateSchemaTests(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads((ROOT / 'schemas/golden-reference.schema.json').read_text())
        self.validator = Draft202012Validator(self.schema)
        self.templates = {x['id']: x for x in json.loads((ROOT / 'registries/templates.json').read_text())['objects']}
        self.spec = yaml.safe_load((ROOT / 'golden-references/GR-03/spec.yaml').read_text())

    def errors(self, template):
        spec = copy.deepcopy(self.spec)
        spec['template'] = template
        return validate_spec(spec, self.templates, self.validator)

    def test_canonical_and_legacy(self):
        for ref in [{'id': 'TPL-CONCEPT-01'}, 'TPL-CONCEPT-01',
                    {'id': 'TPL-COURSE-ENTRY-01', 'variant': 'editorial-split-illustrated'},
                    {'id': 'TPL-COURSE-ENTRY-01'}]:
            with self.subTest(ref=ref):
                self.assertEqual(self.errors(ref), [])

    def test_malformed_references(self):
        for ref in [None, 42, [], {}, {'variant': 'x'}, {'id': 3}, {'id': ''}, '',
                    {'id': 'TPL-CONCEPT-01', 'variant': None},
                    {'id': 'TPL-CONCEPT-01', 'variant': ''},
                    {'id': 'TPL-CONCEPT-01', 'extra': True}]:
            with self.subTest(ref=ref):
                self.assertTrue(self.errors(ref))

    def test_unknown_template(self):
        for ref in ['TPL-UNKNOWN', {'id': 'TPL-UNKNOWN'}]:
            self.assertIn('unknown template', ' '.join(self.errors(ref)))

    def test_unknown_or_wrong_template_variant(self):
        for ref in [{'id': 'TPL-CONCEPT-01', 'variant': 'editorial-split-illustrated'},
                    {'id': 'TPL-COURSE-ENTRY-01', 'variant': 'professional-judgement-dark-evidence'}]:
            self.assertIn('unknown template variant', ' '.join(self.errors(ref)))

    def test_full_spec_schema_is_enforced(self):
        for field in self.schema['required']:
            spec = copy.deepcopy(self.spec)
            del spec[field]
            self.assertTrue(validate_spec(spec, self.templates, self.validator))
        for value in [None, [], 'not a mapping']:
            self.assertTrue(validate_spec(value, self.templates, self.validator))

    def test_episode_delegates_to_authoritative_schema_offline(self):
        episode = json.loads((ROOT / 'schemas/episode.schema.json').read_text())
        self.assertEqual(episode['$ref'], 'golden-reference.schema.json')
        self.assertNotIn('properties', episode)
        episode['$id'] = (ROOT / 'schemas/episode.schema.json').as_uri()
        registry = Registry().with_resource((ROOT / 'schemas/golden-reference.schema.json').as_uri(), Resource.from_contents(self.schema))
        validator = Draft202012Validator(episode, registry=registry)
        for template in [{'id': 'TPL-CONCEPT-01'}, 'TPL-CONCEPT-01', {}, 1]:
            spec = {**self.spec, 'template': template}
            self.assertEqual(validator.is_valid(spec), self.validator.is_valid(spec))

    def test_current_repository(self):
        result = validate_repository()
        self.assertEqual(result['errors'], [])
        self.assertEqual(result['checked'], ['GR-01', 'GR-02', 'GR-03', 'GR-04', 'GR-05', 'GR-06', 'TRACK-A'])
        self.assertEqual(result['legacy_template_strings'], ['GR-02'])

    def test_repository_discovers_and_rejects_invalid_specs(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for directory in ['registries', 'schemas', 'locked-build-specs', 'assets', 'governance', 'prototype-specs']:
                shutil.copytree(ROOT / directory, root / directory)
            for spec in (ROOT / 'golden-references').glob('*/spec.yaml'):
                target = root / spec.relative_to(ROOT)
                target.parent.mkdir(parents=True)
                shutil.copyfile(spec, target)
            extra = root / 'golden-references/GR-TEST'
            extra.mkdir()
            path = extra / 'spec.yaml'
            for content in [None, 'template: [', yaml.safe_dump({**self.spec, 'template': 'UNKNOWN'}),
                            yaml.safe_dump({**self.spec, 'template': {'id': 'TPL-CONCEPT-01', 'variant': 'bad'}}),
                            yaml.safe_dump({**self.spec, 'components': 42})]:
                with self.subTest(content=content):
                    if content is not None:
                        path.write_text(content)
                    result = validate_repository(root)
                    self.assertEqual(result['status'], 'fail')
                    self.assertTrue(any('GR-TEST/spec.yaml' in error for error in result['errors']))


if __name__ == '__main__':
    unittest.main()
