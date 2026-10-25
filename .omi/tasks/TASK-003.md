---
id: TASK-003
title: Add --tip percentage
status: planned
depends: TASK-002
scope: src/split_bill/**, tests/**
---
## Goal
`--tip P` adds P% to the bill before splitting, tip rounded to the nearest đồng (half up).

## Acceptance criteria
- [ ] `split-bill 450000 --people 4 --tip 10` → total 495000, each 123750.
- [ ] Tip rounding half up: `split-bill 15 --people 1 --tip 10` → 17 (1.5 → 2).
- [ ] Negative tip → stderr error, exit code 2. `--tip 0` equals no tip.
- [ ] Unittests cover the above.

## Checkpoint
Done:
Not done:
Tests:
Next:
