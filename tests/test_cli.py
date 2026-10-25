import contextlib
import io
import os
import sys
import unittest

# ponytail: src-layout without install; drop once tests always run after pip install
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from split_bill.cli import main  # noqa: E402
from split_bill.core import split_equal  # noqa: E402


class CliSmokeTest(unittest.TestCase):
    def test_help_exits_zero_and_shows_amount(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            with self.assertRaises(SystemExit) as cm:
                main(["--help"])
        self.assertEqual(cm.exception.code, 0)
        self.assertIn("usage: split-bill", out.getvalue())
        self.assertIn("amount", out.getvalue())


def run(*argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = main(list(argv))
        except SystemExit as e:
            code = e.code
    return code, out.getvalue(), err.getvalue()


class EqualSplitTest(unittest.TestCase):
    def test_pure_function(self):
        self.assertEqual(split_equal(450000, 4), [112500] * 4)
        self.assertEqual(split_equal(100000, 3), [33334, 33333, 33333])

    def test_even(self):
        code, out, _ = run("450000", "--people", "4")
        self.assertEqual(code, 0)
        self.assertEqual(
            out.splitlines(),
            [f"Người {i}: 112500" for i in range(1, 5)] + ["Tổng: 450000"],
        )

    def test_remainder(self):
        code, out, _ = run("100000", "--people", "3")
        self.assertEqual(code, 0)
        self.assertEqual(
            out.splitlines(),
            ["Người 1: 33334", "Người 2: 33333", "Người 3: 33333", "Tổng: 100000"],
        )

    def test_errors_exit_2(self):
        for argv in (
            ["0", "--people", "2"],
            ["-5", "--people", "2"],
            ["12.5", "--people", "2"],
            ["abc", "--people", "2"],
            ["100", "--people", "0"],
            ["100"],
        ):
            code, out, err = run(*argv)
            self.assertEqual(code, 2, argv)
            self.assertEqual(out, "")
            self.assertTrue(err, argv)


if __name__ == "__main__":
    unittest.main()
