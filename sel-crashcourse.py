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

PATH = 'D:\Programming\chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://google.com')
assert 'Google' in driver.title
googleSearch = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
googleSearch.send_keys('hihi wait no let me delete this')
googleSearch.clear()
googleSearch.send_keys('test', Keys.ENTER)
