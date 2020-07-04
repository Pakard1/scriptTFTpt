import time
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # Optional argument, if not specified will search path.
driver.get('http://www.lolchess.gg/')

print(driver.title)


""" time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit() """