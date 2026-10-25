---
id: TASK-001
title: Project skeleton, packaging and CI
status: review
depends:
scope: pyproject.toml, src/split_bill/**, tests/**, .github/workflows/**, README.md, .gitignore
---
## Goal
An installable `split-bill` package (stdlib only) with an `argparse` CLI stub, a unittest suite, and GitHub Actions CI on Ubuntu/Windows/macOS with Python 3.11.

## Acceptance criteria
- [x] `pyproject.toml` (setuptools, src layout, `requires-python >=3.11`, no runtime deps) with console script `split-bill = split_bill.cli:main`.
- [x] `pip install .` then `split-bill --help` exits 0 and shows usage with positional `amount`.
- [x] `python -m unittest discover -s tests` runs and passes (at least one smoke test calling `main(["--help"])` or similar).
- [x] `.github/workflows/ci.yml` runs the tests on push/PR, matrix ubuntu/windows/macos-latest, Python 3.11.
- [x] README.md shows install via `pip install git+https://github.com/omi-teams/omi-pilot-splitbill@staging` and the test command.

## Checkpoint
Done: pyproject.toml, src/split_bill argparse stub, unittest smoke test, CI workflow, README, .gitignore. Verified pip install . and split-bill --help.
Not done: none. CI not run remotely (no remote configured).
Tests: python -m unittest discover -s tests -> 1 test OK.
Next: reviewer.
