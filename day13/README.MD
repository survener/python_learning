# Day13 - Goal

## Main Goal
Improve error handling design with custom exceptions and safer JSON loading.

## Learning Objectives
1. Define and use custom exception classes.
2. Handle invalid JSON input gracefully.
3. Keep business logic predictable under failure.
4. Add tests for failure paths, not only success paths.

## Practical Targets
1. Add custom exceptions in `day09/todo_store.py`.
2. Raise clear errors for invalid JSON format.
3. Add tests for invalid JSON and save/load flow.

## Done Criteria
- `pytest -q day09` passes.
- Invalid JSON is handled with explicit custom exception.
- Changes are committed on `feature/day13-error-handling`.

---

# English Explanation

**Explanation**
- /ˌek.spləˈneɪ.ʃən/

**gracefully**
- 优雅地、妥善地（不让程序崩溃）

**Raise**
- 在编程里通常指 抛出（异常）

**custom exception**
* Example:
```
class InvalidJSONError(Exception):
    pass


def parse_json(text):
    import json
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise InvalidJSONError("Invalid JSON format")
```

**explicit**
- 明确的、显式的



