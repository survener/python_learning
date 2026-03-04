# Phase 2 (14-Day Plan): Python + Git Collaboration

**Goal**

- Write cleaner, modular Python code
- Improve test quality
- Use real Git team workflow (branch → PR-style review → merge)

**Daily Structure (2–3 hours)**
1. 40 min learning
2. 60–90 min coding
3. 20–30 min Git workflow

---
## Week 1 (Days 11–17): Code Quality + Design

**1. Day 11: Project structure**
- Topics: package layout, imports, `__init__.py`  
- Task: refactor one day folder into package style
- Git: feature branch + merge commit message quality

**2. Day 12: Type hints**
- Topics: list[str], dict[str, int], Optional
- Task: add type hints to day08 and day09
- Git: small atomic commits

**3. Day 13: Error handling design**
- Topics: custom exceptions, error boundaries
- Task: improve day09 error handling (invalid JSON, bad path)
- Git: revert practice on one intentional bad commit

**4. Day 14: Logging**
- Topics: logging module, log levels
- Task: add logging to todo persistence flow
- Git: compare commits with git show, git diff

**5. Day 15: OOP improvement**
- Topics: dataclass, encapsulation
- Task: migrate StudentManager records to @dataclass
- Git: branch naming convention + cleanup

**6. Day 16: Testing depth**
- Topics: edge cases, fixtures, parametrization
- Task: raise total tests to 45+
- Git: clean history (amend/reword local only)

**7. Day 17: Mini review day**
- Task: run full test suite, fix weak spots
- Output: short technical review note in day17/README.md
---
## Week 2 (Days 18–24): Mini Real-World Workflow
**1. Day 18–19: CLI v2**
- Add delete/edit/search task features
- Keep tests green

**2. Day 20: File versioning**
- Add simple backup file before save

**3. Day 21: Config support**
- Read settings from .env or config file

**4. Day 22: Documentation quality**
- Write clear README: setup, usage, examples

**5. Day 23: Simulated PR workflow**
- Create feature branch
- Write PR-style summary in markdown
- Merge after self-review checklist

**6. Day 24: Final wrap-up**
- Final test run
- Git history check
- Release tag: v0.1.0


# 英语注释
**Collaboration**
 - /kəˌlæbəˈreɪʃən/ 合作；协作；共同完成某事

**modular**
 - /ˈmɒdʒələr/ 模块化的；由独立单元组成的；可拆分组合的
 - modular design 模块化设计;
 - modular architecture 模块化架构

**PR-style review**
 - PR 指的是 Pull Request，常见于 GitHub、GitLab、Bitbucket 这类 Git 托管平台。
 - 以“Pull Request（PR）”为核心的代码评审流程。

**Daily Structure**
 - 每日结构 / 每日安排框架 / 一天的组织方式

**package layout**
 - 包结构设计
 - src-based package layout
 - flat layout

**refactor**
 - 重构（不改变功能，只优化结构）

**package style**
 - 包式结构（Python package layout）

**Type hints**
 - 类型提示；在 Python 中标注变量、函数参数和返回值的预期类型。
 - ```def greet(name: str) -> str:
    return f"Hello, {name}!"```
**small atomic commits**
 - 小而原子化的提交
 - ``` # ❌ 错误示范：修 bug 顺便改代码格式
git add bug_fix.py style_fix.py
git commit -m "fix bug and format code"

# ✅ 正确示范：分开提交
git add bug_fix.py
git commit -m "fix off-by-one bug in index calculation"

git add style_fix.py
git commit -m "format bug_fix.py according to PEP8" ```

**custom exceptions**
 - 自定义异常

**error handling**
 - 错误处理

**revert**
 - “撤销”或“回滚”

**intentional commit**
 - 故意的提交

**Persistence flow**
 - 数据从“内存/临时状态” → “持久化存储”的流程和步骤。

**OOP improvement**
 - 面向对象改进

**Encapsulation**
 - 封装
 - dataclass：快速定义数据类，自动生成 init/repr/eq
 - 封装：隐藏内部实现，通过方法控制访问
 - dataclass + 封装：dataclass 管理数据结构，封装提供访问控制

**branch naming convention**
 - 分支命名规范
 - | 类型    | 前缀            | 用途      | 示例                         |
| ----- | ------------- | ------- | -------------------------- |
| 功能分支  | `feature/`    | 开发新功能   | `feature/day15-oop`        |
| 修复分支  | `fix/`        | 修复 bug  | `fix/login-bug`            |
| 改进/优化 | `improve/`    | 重构或性能优化 | `improve/data-persistence` |
| 热修复   | `hotfix/`     | 紧急线上修复  | `hotfix/crash-on-startup`  |
| 发布分支  | `release/`    | 准备版本发布  | `release/v1.2.0`           |
| 实验/临时 | `experiment/` | 临时尝试    | `experiment/new-ui`        |

**Testing depth**
 - 测试深度
 - 浅层测试（shallow testing）：只测试表面功能、主要用例
 - 深层测试（deep testing）：测试边界条件、异常情况、内部逻辑

**Fixtures**
 - 测试固件/预置条件
 - 在测试中，用来准备测试环境或测试数据的工具/函数。

**Parametrization**
 - 参数化（测试）
 - 让同一个测试函数可以用不同输入数据重复执行，提高测试覆盖率。

**weak spots**
 - 薄弱点、弱环节、不强的部分

**Mini Real-World Workflow**
 - 一个精简版的真实开发流程

