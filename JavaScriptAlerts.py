from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = "http://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)
browser.maximize_window()

# For "Click for JS Alert" button
"""
AlertButton = browser.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
AlertButton.click()
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(5)
alert.accept()
time.sleep(5)"""

# For "Click for JS Confirm" button
"""AlertButton = browser.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
AlertButton.click()
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(5)
alert.dismiss()
time.sleep(5)"""

# For "Click for JS Prompt" button
AlertButton = browser.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
AlertButton.click()
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(5)
alert.send_keys("This is Selenium with python tutorial on Handling Alerts")
alert.accept()
time.sleep(5)
