from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://selenium.dev/")
driver.maximize_window()
title = driver.title
print(title)
assert "Selenium123" in title

