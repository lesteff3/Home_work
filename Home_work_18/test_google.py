from selenium import webdriver
import unittest




DRIVER_PATH = '/home/user/Рабочий стол/Home_work/Home_work_18/chromedriver'
GOOGLE_URL = 'https://www.google.com/'


class GoogleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)

    def terDown(self) -> None:
        self.driver.close()

    def test_google_title(self):
        self.driver.get(GOOGLE_URL)
        self.assertEqual(self.driver.title, 'Google')


if __name__ == '__main__':
    unittest.main()

