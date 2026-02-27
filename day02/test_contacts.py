from contacts import add_contact, find_contact, list_contacts


def test_add_and_find():
    book = {}
    add_contact(book, "Alice", "123")
    assert find_contact(book, "Alice") == "123"


def test_find_missing():
    book = {}
    assert find_contact(book, "Bob") == "未找到联系人"


def test_list_contacts():
    book = {}
    add_contact(book, "Alice", "123")
    add_contact(book, "Bob", "456")
    rows = list_contacts(book)
    assert "Alice: 123" in rows
    assert "Bob: 456" in rows

"""
每个测试都自己创建 book = {}，避免相互影响。
test_add_and_find：验证“添加后可查到”。
test_find_missing：验证“查无此人”提示。
test_list_contacts：验证列表输出包含联系人字符串。
"""