import contextlib
import io
import os
import sys
import unittest

# ponytail: src-layout without install; drop once tests always run after pip install
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from split_bill.cli import main  # noqa: E402


class CliSmokeTest(unittest.TestCase):
    def test_help_exits_zero_and_shows_amount(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            with self.assertRaises(SystemExit) as cm:
                main(["--help"])
        self.assertEqual(cm.exception.code, 0)
        self.assertIn("usage: split-bill", out.getvalue())
        self.assertIn("amount", out.getvalue())


if __name__ == "__main__":
    unittest.main()
