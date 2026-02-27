Python + Git 10天学习计划
主目录：python_learning
- day01 ~ day10 每天一个目录
- 每天包含 Python 学习 + Git 实操



**总目标（10天后）**
1. 能独立写中小型 Python 脚本（函数、模块、文件处理、异常、简单面向对象）
2. 能用 Git 完成日常开发（分支、合并、冲突解决、回滚、推送）

**每天建议投入**
- 2~3 小时
- 结构：`学习 40% + 编码 40% + Git练习 20%`

---

### Day 1：环境与基础语法
- Python：变量、类型、输入输出、运算、条件语句
- Git：`init / status / add / commit / log`
- 产出：`day01_calculator.py`（四则运算小程序）+ 3 次 commit

### Day 2：循环与容器
- Python：`for/while`、列表/元组/字典/集合
- Git：`.gitignore`、提交规范
- 产出：通讯录程序（内存版）+ 正确忽略 `.venv`、`__pycache__`

### Day 3：函数与模块
- Python：函数定义、参数、返回值、作用域、导入
- Git：分支创建与合并（`switch -c`、`merge`）
- 产出：工具函数库 `utils.py` + `feature` 分支合并一次

### Day 4：字符串与文件
- Python：字符串处理、读写文本/JSON 文件
- Git：撤销未提交改动（`restore`、`restore --staged`）
- 产出：日志清洗脚本（读文件->清洗->写文件）

### Day 5：异常与调试
- Python：`try/except`、自定义错误提示
- Git：`commit --amend`、`reset --soft/mixed`（仅本地）
- 产出：健壮输入处理脚本 + 2 次“故意错误再修复”演练

### Day 6：面向对象基础
- Python：类、对象、方法、封装
- Git：`revert`（已提交后安全撤销）
- 产出：学生管理类 `StudentManager` + 一次 `revert` 演练

### Day 7：测试入门
- Python：`pytest`、测试函数、断言、参数化
- Git：测试驱动提交（先测试后实现）
- 产出：`test_*.py` 至少 8 条测试，全部通过

### Day 8：小项目实战（上）
- Python：命令行项目结构、模块拆分
- Git：功能分支协作流程
- 产出：项目 v1（如“任务管理CLI”）+ README 初稿

### Day 9：小项目实战（下）
- Python：重构、错误处理、文件持久化
- Git：冲突制造与解决、`reflog` 找回误操作
- 产出：项目 v2 + 冲突解决记录一次

### Day 10：总结与发布
- Python：代码整理、注释、文档
- Git：推送 GitHub、整理提交历史
- 产出：完整仓库（可运行、可测试、可阅读）+ 学习总结文档

---

**每天固定验收标准（必须完成）**
1. 当天代码可运行  
2. 当天至少 1 个 Git 主题被实际操作  
3. 有清晰 commit 信息（`feat/fix/chore/test`）  
4. `git status` 最终干净
