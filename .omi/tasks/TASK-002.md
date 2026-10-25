---
id: TASK-002
title: Equal split with --people, table output and input validation
status: planned
depends: TASK-001
scope: src/split_bill/**, tests/**
---
## Goal
`split-bill <amount> --people N` prints each person's integer VND share as a simple table with a `Tổng` line, per docs/product.md.

## Acceptance criteria
- [ ] `split-bill 450000 --people 4` → 4 rows `Người 1..4` each 112500, then `Tổng` 450000.
- [ ] `split-bill 100000 --people 3` → 33334, 33333, 33333; `Tổng` equals 100000.
- [ ] Amount ≤ 0 or non-integer, and `--people` < 1 → clear message on stderr, exit code 2.
- [ ] Neither `--people` nor `--shares` given → error, exit code 2 (the `--shares` flag itself comes in TASK-005).
- [ ] Split logic is a pure function with unittests for the cases above; CLI tested via `main(argv)`.

## Checkpoint
Done:
Not done:
Tests:
Next:
