from func_file import get_doc_owner_name, get_all_doc_owners_names, add_new_shelf, delete_doc
import unittest


class HwFuncTest(unittest.TestCase):

    def test_doc_owner_name(self):
        # проверка работоспособности функции (функция находит значение)
        self.assertEqual(get_doc_owner_name('2207 876234'), 'Василий Гупкин')

    def test_doc_owners_names(self):
        # проверка корректности формирования уникальных записей
        self.assertIsInstance(get_all_doc_owners_names(), set)

    def test_add_new_shelf(self):
        # проверка корректности создание полки/полок
        self.assertEqual(type(add_new_shelf(5)[0]), int)

    """def test_add_new_shelf(self):
        # проверка корректности создание полки/полок 
        # (альтернативная версия с пользовательским вводом значения полки для проверки ввода текстовых значений)
        self.assertEqual(type(add_new_shelf()[0]), int)"""

    def test_delete_doc(self):
        # проверка работоспособности функции удаления документов
        self.assertEqual(delete_doc('10006')[1], True)


if __name__ =='__main__':
    unittest.main()