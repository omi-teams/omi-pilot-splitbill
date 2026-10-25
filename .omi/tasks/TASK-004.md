---
id: TASK-004
title: Add --round up to multiple with surplus line
status: planned
depends: TASK-003
scope: src/split_bill/**, tests/**
---
## Goal
`--round N` rounds each person's share up to a multiple of N and prints a `Dư` line (sum paid − bill after tip) below `Tổng`.

## Acceptance criteria
- [ ] `split-bill 100000 --people 3 --round 1000` → each 34000, `Tổng` 102000, `Dư` 2000.
- [ ] Already-multiple shares are unchanged: `450000 --people 4 --round 500` → each 112500, `Dư` 0.
- [ ] Works combined with `--tip`.
- [ ] `--round` ≤ 0 → stderr error, exit code 2.
- [ ] Unittests cover the above.

## Checkpoint
Done:
Not done:
Tests:
Next:
