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
        self._driver.get('https://www.linkedin.com/in/{}'.format(self._username))

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
        positions = self._driver.find_elements(By.XPATH, "div[@class='pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested']\
                                                         /div[@class='display-flex flex-column full-width align-self-center']\
                                                         /div\
                                                         /div[@class='display-flex flex-column full-width']\
                                                         /div/span/span[@aria-hidden='true']")

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

        # exp_index = position_arr.index('Experience')
        # for i in range(exp_index):
        #     position_arr.pop(0)
        #
        # edu_index = position_arr.index('Education')
        # l = len(position_arr)
        # for i in range(l - edu_index + 1):
        #     position_arr.pop(edu_index-1)
        #
        # experience = {
        #     'positions': [],
        #     'organisations': [],
        #     'commitment': [],
        #     'date_duration': [],
        # }
        #
        # counter = 1
        # for index, item in enumerate(position_arr):
        #     if index == 0:
        #         continue
        #     if counter == 1:
        #         experience['positions'].append(item)
        #         counter += 1
        #     elif counter == 2:
        #         experience['organisations'].append(item)
        #         counter += 1
        #     elif counter == 3:
        #         experience['commitment'].append(item)
        #         counter += 1
        #     elif counter == 4:
        #         experience['date_duration'].append(item)
        #         counter = 1


        # print(experience)


g = GetLinkedinData('amandalowyx')
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
