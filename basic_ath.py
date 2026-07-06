from selenium import webdriver
import time

username = "admin"
password = "admin"

browser = webdriver.Chrome()
browser.maximize_window()
url = "http://admin:admin@the-internet.herokuapp.com/basic_auth"
browser.get(url)
time.sleep(5)


# https://username:password@domain/path
