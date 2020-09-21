from yandex_requests import YaFolderMaker
import unittest


token = ''


class HwFuncTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Ya = YaFolderMaker(token)

    @unittest.skipIf(YaFolderMaker(token).make_folder() == 201, "folder was created right now")
    def test_make_folder(self):
        # проверка работоспособности процесса создания папки
        self.assertEqual(self.Ya.make_folder(), 200)

    def test_wrong_args(self):

        self.assertRaises(ValueError, self.Ya.make_folder(), 200)