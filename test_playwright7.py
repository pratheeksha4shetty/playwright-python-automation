import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get(r"https://demoapps.qspiders.com/ui/dragDrop/dragToCorrect?sublist=2")
driver.maximize_window()
time.sleep(2)
ob=ActionChains(driver)

mobile_charger=driver.find_element("xpath",'//div[text()="Mobile Charger"]')
laptop_charger=driver.find_element("xpath",'//div[text()="Laptop Charger"]')
mobile_cover=driver.find_element("xpath",'//div[text()="Mobile Cover"]')
laptop_cover=driver.find_element("xpath",'//div[text()="Laptop Cover"]')

mobile=driver.find_element("xpath",'//*[@id="demoUI"]/main/section/article/aside/div/aside/div/div/div/section[2]/div[1]')
laptop=driver.find_element("xpath",'//*[@id="demoUI"]/main/section/article/aside/div/aside/div/div/div/section[2]/div[2]')

ob.drag_and_drop(mobile_charger,mobile).perform()
ob.drag_and_drop(laptop_charger,laptop).perform()
ob.drag_and_drop(mobile_cover,mobile).perform()
ob.drag_and_drop(laptop_cover,laptop).perform()

time.sleep(2)