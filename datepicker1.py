from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://www.globalsqa.com/demo-site/datepicker/"
browser.get(url)

browser.find_element(By.XPATH, "//div[@rel-title='Simple Date Picker']//div//a").click()
frameLo = browser.find_element(By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame']")
browser.switch_to.frame(frameLo)
time.sleep(5)

browser.find_element(By.CSS_SELECTOR, "#datepicker").click()
current_date = datetime.now() #Current Date

next_date = current_date + timedelta(days=1)

formatted_date = next_date.strftime("%m/%d/%y")

browser.find_element(By.CSS_SELECTOR, "#datepicker").send_keys(formatted_date + Keys.TAB)
time.sleep(5)
browser.quit()
