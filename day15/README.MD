# Day15 - Goal

## Main Goal
Refactor the student manager model using `dataclass` to improve clarity and structure.

## Learning Objectives
1. Understand what `@dataclass` solves.
2. Replace loose dictionaries with a typed data model.
3. Keep current behavior while improving code design.
4. Verify refactoring with tests.

## Practical Targets
1. Create a `Student` dataclass.
2. Refactor `StudentManager` to store `Student` objects.
3. Update tests to validate the new structure.
4. Keep `pytest -q day06` passing.

## Done Criteria
- Student records use `@dataclass`
- Tests pass
- Refactor is committed on a feature branch


---


# English Explanation

**loose dictionaries**
* 松散的字典结构
```
task = {
    "title": "Buy milk",
    "done": False
}

这种随意定义的dict:
key 没有强约束
类型不明确
容易拼写错误
IDE 无法很好提示
```

