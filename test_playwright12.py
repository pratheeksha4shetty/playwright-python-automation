#playwright
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")

    page.wait_for_selector("a")

    all_links_count = page.locator("a").count()
    print("Total <a> tags:", all_links_count)

    visible_links_count = page.get_by_role("link").count()
    print("Total visible links:", visible_links_count)

    browser.close()



#selenium
import time 
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

links=driver.find_elements("tag name",'a')
print(len(links))
time.sleep(2)

#images
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

images=driver.find_elements("tag name",'img')
print(len(images))
time.sleep(2)

# buttons
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

buttons = driver.find_elements("tag name", "button")
print("Total buttons:", len(buttons))
time.sleep(3)
driver.quit()


# frames
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

frames = driver.find_elements("tag name", "iframe")
print("Total frames:", len(frames))
time.sleep(3)
driver.quit()
