from task_1 import get_name, get_directory, add_doc, delete_doc

def test_get_name():
    assert get_name("10006") == "Аристарх Павлов"


def test_get_directory():
    assert get_directory("11-2") == "1"


def test_add():
    add_doc('international passport', '311 020203', 'Александр Пушкин', 3)
    assert get_directory("311 020203") == "3"
    assert get_name("311 020203") == "Александр Пушкин"

def test_delete_document():
    assert delete_doc('2207 876234') == "Документ 2207 876234 удален"
    assert delete_doc('101') == "Документ 101 не найден"
