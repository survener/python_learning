# Day10 收官总结（Python + Git）

## 1. 学习成果总览
- Day01: 计算器 + 基础测试
- Day02: 通讯录（内存版）+ 测试
- Day03: 工具函数模块 + 测试
- Day04: 日志清洗（文件读写）+ 测试
- Day05: 异常处理输入守卫 + 测试
- Day06: StudentManager（面向对象）+ 测试
- Day07: 参数化测试
- Day08: Todo CLI v1 + 测试
- Day09: Todo JSON 持久化 + 测试 + README 图片

## 2. Git 能力清单（已实践）
- init / add / commit / push / pull --rebase
- branch / switch / merge
- 冲突处理与重新合并
- reset --soft（撤回提交保留改动）
- .gitignore 管理（.venv/.idea/__pycache__）

## 3. 典型问题与解决
1) pip SSL 证书失败 -> 安装证书脚本后恢复
2) 误提交 .venv/.idea -> .gitignore + git rm --cached 清理
3) Repository not found -> 修正远程地址并先创建 GitHub 仓库
4) merge 冲突导致测试失败 -> reset 回退并正确解决冲突
5) README 图片不显示 -> 修正相对路径

## 4. 当前待提升
- 进一步练习 reflog / revert 场景
- 为 day08/day09 增加更多异常分支测试
- 引入简单 CI（如 GitHub Actions 跑 pytest）

## 5. 下一阶段（建议 7 天）
- 数据结构与算法基础（列表/哈希/栈队列）
- Python 标准库强化（pathlib/json/datetime）
- 小项目重构（分层、类型注解、日志）