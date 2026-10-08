import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / 'bundle'
SOURCE = (BUNDLE / 'main.splash').read_text()

class ReleaseContract(unittest.TestCase):
    def test_date_range_requires_host_window_metadata(self):
        helper = SOURCE.split('fn range_label(data){', 1)[1].split('fn reset_chat()', 1)[0]
        self.assertIn('data.window', helper)
        self.assertIn('bounds.time_min', helper)
        self.assertIn('bounds.time_max', helper)
        self.assertIn('if bounds == nil { return "date range unavailable" }', helper)
        self.assertIn('first == nil || last == nil || first == "" || last == ""', helper)
        self.assertIn('past 30 days / next 366 days', helper)

    def test_cached_and_refreshed_agenda_are_not_claimed_to_be_the_whole_calendar(self):
        cached = SOURCE.split('fn load_cache(){', 1)[1].split('fn refresh(){', 1)[0]
        refresh = SOURCE.split('fn refresh(){', 1)[1].split('fn render_detail(){', 1)[0]
        self.assertIn('agenda_range = range_label(r.data)', cached)
        self.assertIn('agenda_range = range_label(r.data)', refresh)
        self.assertIn('"Cached · " + agenda_range', cached)
        self.assertIn('" events · " + agenda_range', refresh)
        self.assertIn('cached agenda kept · " + agenda_range', refresh)
        self.assertNotIn('The selected event is no longer in this calendar.', SOURCE)
        self.assertIn('may be outside the displayed date range', refresh)

    def test_layout_original_pixels_and_read_only_tools_are_preserved(self):
        prior = json.loads((ROOT / 'review/releases/0.1.0/RELEASE.json').read_text())['release_files_sha256']
        for name, digest in prior.items():
            if name in ('AGENT.md', 'tools.json') :
                self.assertEqual(hashlib.sha256((BUNDLE / name).read_bytes()).hexdigest(), digest, name)
        self.assertEqual(hashlib.sha256(SOURCE[SOURCE.index('let ink = '):].encode()).hexdigest(), '77e870d8b7b52dc04439cd610b3873f03e9681e4f482e84ac2bb187d4bb7a55d')
        manifest = json.loads((BUNDLE / 'manifest.json').read_text())
        self.assertEqual(manifest['version'], '0.2.1')
        self.assertEqual(manifest['id'], 'io.github.ymote.googlecalendar')
        self.assertNotIn('org.octosense.samples.googlecalendar', SOURCE)
        self.assertIn('app://io.github.ymote.googlecalendar/', SOURCE)
        self.assertFalse(manifest['agent'].get('background', False))
        self.assertEqual(manifest['network']['hosts'], [])
        self.assertEqual(json.loads((BUNDLE / 'listing.json').read_text())['platforms'], ['macos'])

if __name__ == '__main__': unittest.main()
