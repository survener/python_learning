def add_task(task_list, task_title):
    task_list.append({"title": task_title, "done": False})


def list_tasks(task_list):
    lines = []
    for i, task in enumerate(task_list, start=1):
        mark = "x" if task["done"] else " "
        lines.append(f"{i}. [{mark}] {task['title']}")
    return lines


def finish_task(task_list, index):
    if index < 1 or index > len(task_list):
        return False
    task_list[index - 1]["done"] = True
    return True


if __name__ == "__main__":
    tasks = []
    while True:
        cmd = input("命令(add/list/done/exit): ").strip().lower()

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
        elif cmd == "exit":
            print("退出")
            break
        else:
            print("不支持的命令")
