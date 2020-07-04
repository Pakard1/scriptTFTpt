import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # Optional argument, if not specified will search path.
driver.get('https://tracker.gg/tft/profile/riot/EUW/ArtourBabaevsky/overview')

print(driver.title)


select = driver.find_element_by_class_name("dropdrown__items")
select.select_by_visible_text("EU (West)")

search = driver.find_element_by_name("Search Summoner")
search.send_keys("ArtourBabaevsky")
search.send_keys(Keys.RETURN)
#search.submit() """

time.sleep(5) # Let the user actually see something!

driver.quit() 