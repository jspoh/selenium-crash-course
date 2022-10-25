# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pickle
from csv import DictReader

# MAKE IT SO THAT THE SELENIUM BROWSER DOES NOT POP OUT
options = Options()
# options.add_argument("--headless")

class GetLinkedinData:
    def __init__(self, username: str):
        self._driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self._username = username

    def close_driver(self):
        self._driver.close()

    def remove_duplicates(self, arr):
        new_arr = []
        for item in arr:
            if item.text not in new_arr:
                new_arr.append(item.text)
        return new_arr

    def open_user_page(self):
        self._driver.get('https://www.linkedin.com/in/{}/details/experience'.format(self._username))

        cookie_list = self.get_cookies('linkedin_cookies.csv')
        for cookie in cookie_list:
            self._driver.add_cookie(cookie)

        print('cookies added. refreshing..')
        self._driver.refresh()

        time.sleep(7)

    def get_cookies(self, file):
        print('getting cookies..')
        with open(file, encoding='utf-8-sig') as f:
            dict_reader = DictReader(f)
            dict_list = list(dict_reader)
        return dict_list

    def get_experiences(self):
        position_arr = []
        print('getting experiences..')
        positions = self._driver.find_elements(By.XPATH, "//span[@class='visually-hidden']")  # this works

        for position in positions:
            print(position.text)
            try:
                pos = position.text.split('\n')
                if pos[0] not in position_arr:
                    position_arr.append(pos[0])
            except Exception:
                if position.text not in position_arr:
                    position_arr.append(position.text)

        print(position_arr)


# g = GetLinkedinData('rvi-test-491644253')
# g = GetLinkedinData('js-poh')
g = GetLinkedinData('dinghanlim')
g.open_user_page()
g.get_experiences()
g.close_driver()


# # INPUT USERNAME
# email_input = self._driver.find_element(By.XPATH, "//input[@id='username']")
# email_input.send_keys(self.__login_id)
#
# # INPUT PASSWORD
# pw_input = self._driver.find_element(By.XPATH, "//input[@id='password']")
# pw_input.send_keys(self.__pw, Keys.ENTER)
# time.sleep(3)
