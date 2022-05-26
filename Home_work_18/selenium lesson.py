from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from logger import get_logger


logger = get_logger()



SUBSCRIBERS = 'logger.txt'
DRIVER_PATH = '/home/user/Рабочий стол/Home_work/Home_work_18/chromedriver'
GOOGLE_URL = 'https://www.google.com/'



class Twitter:

    def __init__(self, executable_path: str, person_name: str):
        self.driver = webdriver.Chrome(executable_path=executable_path)
        self._find_necessary_person(person_name)

    def __enter__(self):
        self.driver.get(GOOGLE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.driver:
            self.driver.close()





    def _find_necessary_person(self, username: str):
        self.driver.get(GOOGLE_URL)
        found_element = self.driver.find_element_by_xpath('//input[@title="Поиск"]')
        if found_element:
            found_element.send_keys(f'twitter {username}')
            sleep(1)
            found_element.send_keys(Keys.ENTER)
            sleep(1)
            choice_person = self.driver.find_element_by_partial_link_text('Александр Солодуха (@solodukha) / Твиттер - Twitter')
            choice_person.send_keys(Keys.ENTER)
            sleep(1)
            found_sub = self.driver.find_element_by_partial_link_text('читателей')
            subscribers = found_sub.text
            my_file = open('logger.txt', 'w')
            my_file.writelines(subscribers)
            my_file.close()



if __name__ == '__main__':
    with Twitter(executable_path=DRIVER_PATH, person_name='solodukha') as tw:
        pass

