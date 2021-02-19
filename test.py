import unittest

from user_request import get_all_avatars


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'https://reqres.in/api/users'
        self.avatars_result = ['https://reqres.in/img/faces/1-image.jpg', 'https://reqres.in/img/faces/3-image.jpg',
                               'https://reqres.in/img/faces/2-image.jpg', 'https://reqres.in/img/faces/4-image.jpg',
                               'https://reqres.in/img/faces/5-image.jpg', 'https://reqres.in/img/faces/6-image.jpg',
                               'https://reqres.in/img/faces/7-image.jpg', 'https://reqres.in/img/faces/8-image.jpg',
                               'https://reqres.in/img/faces/9-image.jpg', 'https://reqres.in/img/faces/10-image.jpg',
                               'https://reqres.in/img/faces/11-image.jpg', 'https://reqres.in/img/faces/12-image.jpg']

    def test_avatars(self):
        self.assertCountEqual(get_all_avatars(self.url), self.avatars_result)


if __name__ == '__main__':
    unittest.main()
