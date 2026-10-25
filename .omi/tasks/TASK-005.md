---
id: TASK-005
title: Add --shares proportional split
status: planned
depends: TASK-004
scope: src/split_bill/**, tests/**
---
## Goal
`--shares Name=w,...` splits the bill proportionally by integer weights instead of `--people`, remainder đồng to the largest fractional parts (ties by input order).

## Acceptance criteria
- [ ] `split-bill 400000 --shares An=2,Binh=1,Chi=1` → An 200000, Binh 100000, Chi 100000; `Tổng` 400000.
- [ ] Non-divisible case sums exactly to the bill, e.g. `100000 --shares A=1,B=1,C=1` → 33334, 33333, 33333.
- [ ] Works combined with `--tip` and `--round`.
- [ ] Errors (stderr, exit 2): empty shares, bad syntax, weight ≤ 0 or non-integer, duplicate names, both `--people` and `--shares`.
- [ ] Unittests cover the above.

## Checkpoint
Done:
Not done:
Tests:
Next:
