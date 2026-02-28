# Day06：面向对象基础（StudentManager）

## 每日目标
1. 理解类与对象的关系
2. 掌握 `__init__`、实例属性、实例方法
3. 能用类封装一组相关功能（新增/查询/列表）
4. 用 pytest 为类方法编写基础测试

## 学习要点
- 类（class）是模板，对象（object）是实例
- `__init__` 用于初始化对象状态
- 使用方法操作对象内部数据，而不是散落函数

## 实战任务
实现 `StudentManager`：
1. `add_student(name, age)`：添加学生
2. `list_students()`：返回全部学生
3. `find_student(name)`：按姓名查找，找不到返回 `None`

## 代码要求
- 学生数据用列表+字典保存（先不引入数据库）
- 方法命名清晰
- 不写多余逻辑，先保证正确性

## 测试任务
编写 `test_student_manager.py`，至少包含：
1. 添加后能查到学生
2. 查询不存在学生返回 `None`
3. 列表长度与添加数量一致

## Git 任务
1. 新建分支：`feature/day06-oop`
2. 完成代码与测试后提交
3. 合并到 `main` 并推送

## 完成标准（验收）
- `pytest -q day06` 全部通过
- `git status` 最终干净
- GitHub 上可看到 Day06 代码和测试
