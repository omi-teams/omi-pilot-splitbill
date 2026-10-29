"""Command-line entry point."""

import argparse
import sys
from decimal import Decimal, InvalidOperation

from split_bill.core import split_equal


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="split-bill",
        description="Split a restaurant bill.",
    )
    parser.add_argument("amount", help="bill amount in VND (positive integer)")
    parser.add_argument("--people", type=int, help="number of people (>= 1)")
    parser.add_argument("--tip", default="0", help="tip percentage (>= 0)")
    return parser


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):  # Windows consoles default to non-UTF-8
            stream.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args(argv)  # argparse errors exit 2 on stderr
    try:
        amount = int(args.amount)
    except ValueError:
        parser.error(f"amount must be an integer, got {args.amount!r}")
    if amount <= 0:
        parser.error("amount must be greater than 0")
    if args.people is None:
        parser.error("--people is required (or --shares)")
    if args.people < 1:
        parser.error("--people must be at least 1")
    try:
        tip = Decimal(args.tip)
    except InvalidOperation:
        parser.error("--tip must be a non-negative finite percentage")
    if not tip.is_finite() or tip < 0:
        parser.error("--tip must be a non-negative finite percentage")
    numerator, denominator = tip.as_integer_ratio()
    # Integer arithmetic keeps half-up rounding exact for decimal percentages.
    tip_amount = (amount * numerator + 50 * denominator) // (100 * denominator)
    shares = split_equal(amount + tip_amount, args.people)
    for i, s in enumerate(shares, 1):
        print(f"Người {i}: {s}")
    print(f"Tổng: {sum(shares)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
