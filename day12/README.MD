# Day12 - Goal

## Main Goal
Add clear type hints to existing modules and improve readability/maintainability.

## Learning Objectives
1. Use built-in type hints (`list`, `dict`, `str`, `bool`, `int`).
2. Annotate function parameters and return types.
3. Keep behavior unchanged while improving code quality.
4. Ensure tests still pass after refactor.

## Practical Targets
1. Add type hints to `day08/todo_cli.py`.
2. Add type hints to `day09/todo_store.py`.
3. Run related tests and verify no regression.

## Done Criteria
- `pytest -q day08 day09` passes.
- Code remains functionally identical.
- Changes are committed and pushed on a feature branch.

---

#English Explanation

**built-in**
- 内置
- built-in type hints → Python 内置的类型提示

**Annotate**
- /ˈæn.ə.teɪt/
- 标注、注解
- 在 Python 里指使用 类型提示（type hints）

**function parameters**
- 函数参数

*在函数的参数和返回值上加类型注解*

**regression**
- 回归
- 本来正常的功能由于修改或优化而出现错误。

**functionally identical**
- 功能上完全相同
