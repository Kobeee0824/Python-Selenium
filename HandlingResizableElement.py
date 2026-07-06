from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://demo.automationtesting.in/Resizable.html"
browser.get(url)
resizable_element = browser.find_element(By.XPATH, "//div[@id='resizable']//div[3]")
Initial_element_size = browser.find_element(By.XPATH, "//div[@id='resizable']//div[3]")
initial_size = Initial_element_size.size
print("Initial Size: ", initial_size)
time.sleep(5)
action_chains = ActionChains(browser)
action_chains.click_and_hold(resizable_element).move_by_offset(100, 100).release().perform()
time.sleep(5)
resized_element = Initial_element_size.size
print("Resized Element: ", resized_element)
browser.quit()