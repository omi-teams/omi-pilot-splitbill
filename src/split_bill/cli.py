"""Command-line entry point. Stub: only the amount argument for now."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="split-bill",
        description="Split a restaurant bill.",
    )
    parser.add_argument("amount", type=int, help="bill amount in VND (integer)")
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    parser.parse_args(argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
