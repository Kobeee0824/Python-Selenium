from selenium import webdriver
from selenium.webdriver.commonby import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://the-internet.herokuapp.com/nested_frames")

# Switching to TOP Frame
browser.switch_to.frame("frame-top")

# Switching to Middle Frame
browser.switch_to.frame("frame-middle")

content = browser.find_element(By.ID, "content").text
print("Content in middle frame", content)

# Switch to Default content
browser.switch_to.default_content()

# Switch to Bottom Frame
browser.switch_to.frame("frame-bottom")
content_Bottom = browser.find_element(By.TAG_NAME, "body").text
print("Content in B ottom frame", content_Bottom)
