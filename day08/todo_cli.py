def add_task(task_list: list[dict[str, object]], task_title: str) -> None:
    task_list.append({"title": task_title, "done": False})


def list_tasks(task_list: list[dict[str, object]]) -> list[str]:
    lines: list[str] = []
    for i, task in enumerate(task_list, start=1):
        mark = "x" if task["done"] else " "
        lines.append(f"{i}. [{mark}] {task['title']}")
    return lines


def finish_task(task_list: list[dict[str, object]], index: int) -> bool:
    if index < 1 or index > len(task_list):
        return False
    task_list[index - 1]["done"] = True
    return True


def delete_task(task_list: list[dict[str, object]], index: int) -> bool:
    if index < 1 or index > len(task_list):
        return False
    del task_list[index - 1]
    return True


def edit_task(task_list: list[dict[str, object]], index: int, new_title: str) -> bool:
    if index < 1 or index > len(task_list):
        return False
    task_list[index - 1]["title"] = new_title
    return True


def search_tasks(task_list: list[dict[str, object]], keyword: str) -> list[str]:
    keyword = keyword.strip().lower()
    if not keyword:
        return []
    results = []
    for i, task in enumerate(task_list, start=1):
        title = str(task["title"])
        if keyword in title.lower():
            mark = "x" if task["done"] else " "
            results.append(f"{i}. [{mark}] {title}")
    return results


if __name__ == "__main__":
    tasks: list[dict[str, object]] = []
    while True:
        cmd = input("命令(add/list/done/del/edit/search/exit): ").strip().lower()

        if cmd == "add":
            title = input("任务标题: ").strip()
            add_task(tasks, title)
            print("已添加")
        elif cmd == "list":
            for row in list_tasks(tasks):
                print(row)
        elif cmd == "done":
            n = input("完成第几个任务: ").strip()
            if not n.isdigit():
                print("请输入数字")
                continue
            ok = finish_task(tasks, int(n))
            print("已完成" if ok else "任务编号不存在")
        elif cmd == "del":
            n = input("删除第几个任务: ").strip()
            if not n.isdigit():
                print("请输入数字")
                continue
            ok = delete_task(tasks, int(n))
            print("已删除" if ok else "任务编号不存在")
        elif cmd == "edit":
            n = input("编辑第几个任务: ").strip()
            if not n.isdigit():
                print("请输入数字")
                continue
            new_title = input("新标题: ").strip()
            ok = edit_task(tasks, int(n), new_title)
            print("已修改" if ok else "任务编号不存在")
        elif cmd == "search":
            keyword = input("关键词: ").strip()
            for row in search_tasks(tasks, keyword):
                print(row)
        elif cmd == "exit":
            print("退出")
            break
        else:
            print("不支持的命令")
