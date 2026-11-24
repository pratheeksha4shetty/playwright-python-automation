# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False,slow_mo=1000)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://demoapps.qspiders.com/ui?scenario=1")
#     page.get_by_role("textbox", name="Name").click()
#     page.get_by_role("textbox", name="Name").fill("pratheeksha")
#     page.get_by_role("textbox", name="Email Id").click()
#     page.get_by_role("textbox", name="Email Id").fill("pratheekshashetty84")
#     page.get_by_role("textbox", name="Email Id").press("Shift+CapsLock")
#     page.get_by_role("textbox", name="Email Id").fill("pratheekshashetty84@GMAIL.COM")
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("@")
#     page.get_by_role("textbox", name="Password").press("CapsLock")
#     page.get_by_role("textbox", name="Password").fill("@P")
#     page.get_by_role("textbox", name="Password").press("CapsLock")
#     page.get_by_role("textbox", name="Password").fill("@Prathi0908")
#     page.get_by_role("img", name="Show Password").locator("path").click()
#     page.get_by_role("button", name="Register").click()
#     page.get_by_role("textbox", name="Email Id").click()
#     page.get_by_role("textbox", name="Email Id").fill("pratheeksha")
#     page.get_by_role("textbox", name="Email Id").press("CapsLock")
#     page.get_by_role("textbox", name="Email Id").press("CapsLock")
#     page.get_by_role("textbox", name="Email Id").fill("pratheekshashetty84@gmail.com")
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("@")
#     page.get_by_role("textbox", name="Password").press("CapsLock")
#     page.get_by_role("textbox", name="Password").fill("@P")
#     page.get_by_role("textbox", name="Password").press("CapsLock")
#     page.get_by_role("textbox", name="Password").fill("@Prathi0908")
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("img", name="Show Password").locator("path").click()
#     page.get_by_role("button", name="Login").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)

#DISABLED ELEMENTS


import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get(r"https://demoapps.qspiders.com/ui?scenario=1")
driver.maximize_window()
time.sleep(2)
driver.find_element("xpath",'//li[text()="Disabled"]').click()
time.sleep(2)

name=driver.find_element("id","name")
driver.execute_script("arguments[0].removeAttribute('disabled');",name)
name.send_keys('pratheeksha')
time.sleep(2)

email=driver.find_element("id","email")
driver.execute_script("arguments[0].removeAttribute('disabled');",email)
email.send_keys('pratheekshashetty84@gmail.com')
time.sleep(2)

password=driver.find_element("id","password")
driver.execute_script("arguments[0].removeAttribute('disabled');",password)
password.send_keys("@Prathi0908")
time.sleep(3)

register=driver.find_element("xpath","//button[@type='submit']")
driver.execute_script("arguments[0].removeAttribute('disabled');",register)
register.click()
time.sleep(2)