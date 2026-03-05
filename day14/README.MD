# Day14 - Goal

## Main Goal
Introduce logging into the todo storage workflow to improve observability and debugging.

## Learning Objectives
1. Understand Python `logging` basics (`info`, `warning`, `error`).
2. Add meaningful logs at key workflow points (load/save/add/finish).
3. Keep existing behavior unchanged while improving traceability.
4. Verify that tests still pass after non-functional refactoring.

## Practical Targets
1. Add module-level logger in `day09/todo_store.py`.
2. Log normal events:
   - loading tasks
   - saving tasks
   - adding task
   - finishing task
3. Log abnormal events:
   - invalid JSON format
   - non-list JSON data
   - invalid task index
4. Ensure all day09 tests pass.

## Git Targets
1. Work on branch: `feature/day14-logging`
2. Commit with clear message.
3. Push branch and merge into `main` after tests pass.

## Done Criteria
- `python -m pytest -q day09` passes.
- Logging is present and readable.
- No functional regression.
- Branch is merged and synchronized with remote main.


---

# English Explanation

**Introduce logging**
* 引入日志机制

**observability**
* 可观测性

**traceability**
* 可追踪性

**Non-functional refactoring**
* 非功能性重构

**logger**
* 日志记录器对象，用来记录程序运行信息（info、debug、warning、error 等）。