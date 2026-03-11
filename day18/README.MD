# Day18 - Goal

## Main Goal
Extend the todo CLI with delete, edit, and search features (v2).

## Learning Objectives
1. Design small, testable functions for new features.
2. Keep CLI logic separated from core logic.
3. Add tests for new behaviors.

## Practical Targets
1. Add `delete_task`, `edit_task`, `search_tasks`.
2. Update CLI to expose new commands.
3. Add tests covering success + invalid indexes.

## Done Criteria
- `python -m pytest -q day08` passes
- New features work in CLI
- Changes committed on `feature/day18-todo-v2`


---

# English Explanation

**expose**
> 让某个功能 对用户可见
让 API / CLI 可以调用
将内部功能 公开出来
* 即对外提供接口

