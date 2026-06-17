from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://www.google.com"
browser.get(url)

browser.find_element(By.XPATH, "//a[normalize-space()='Gmail']").click()