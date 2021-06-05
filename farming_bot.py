from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5) #Same as time.sleep()
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-1)] #getting list of items by id
actions = ActionChains(driver)
actions.click(cookie)
N=100
for i in range(N):
    actions.perform()
    count = int(cookie_count.text.split()[0])
    for item in items:
        value = int(item.text)
        if value<=count:
            upgrade = ActionChains(driver)
            upgrade.move_to_element(item)
            upgrade.click()
            upgrade.perform()
