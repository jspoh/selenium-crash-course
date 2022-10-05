# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# KEEP WINDOW OPEN AFTER FINISHING OPERATION
options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # initialize a driver
driver.get('https://google.com')  # navigate to page
assert 'Google' in driver.title  # ensure that page is correct
googleSearch = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')  # get element by xpath (there are extensions to help)
googleSearch.send_keys('hihi wait no let me delete this')  # send keystrokes
googleSearch.clear()  # clear input (if its in an input field)
googleSearch.send_keys('test', Keys.ENTER)  # send keystrokes and press enter
