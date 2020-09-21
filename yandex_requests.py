import requests


class YaFolderMaker:

    def __init__(self, token):
        self.BASE_URL = 'https://cloud-api.yandex.net:443'
        self.AUTHOR = {"Authorization": token}
        self.BAS_STRUCTURE_URL = '/v1/disk/resources'

    def make_folder(self, folder_name='Временная'):
        disk_root = {'path': f'/{folder_name}/'}
        result = requests.get(self.BASE_URL + self.BAS_STRUCTURE_URL,
                              params=disk_root, headers=self.AUTHOR)
        if result.status_code == 404:
            result = requests.put(self.BASE_URL + self.BAS_STRUCTURE_URL,
                                  params=disk_root, headers=self.AUTHOR)
        return result.status_code


token = ''
print(YaFolderMaker(token).make_folder('chauchau'))
