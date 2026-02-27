def add_contact(book, name, phone):
    book[name] = phone


def find_contact(book, name):
    return book.get(name, "未找到联系人")


def list_contacts(book):
    return [f"{name}: {phone}" for name, phone in book.items()]


if __name__ == "__main__":
    contacts = {}
    while True:
        cmd = input("命令(add/find/list/exit): ").strip().lower()

        if cmd == "add":
            name = input("姓名: ").strip()
            phone = input("电话: ").strip()
            add_contact(contacts, name, phone)
            print("已添加")
        elif cmd == "find":
            name = input("姓名: ").strip()
            print(find_contact(contacts, name))
        elif cmd == "list":
            for row in list_contacts(contacts):
                print(row)
        elif cmd == "exit":
            print("退出程序")
            break
        else:
            print("不支持的命令")

"""
book 是字典：{姓名: 电话}。
add_contact：新增/覆盖联系人。
find_contact：查找联系人，不存在返回默认提示。
list_contacts：把字典转成可打印字符串列表。
while True：持续接收命令，直到输入 exit
"""