import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # Optional argument, if not specified will search path.
driver.get('https://lolchess.gg')


print(driver.title)


select_dropdown = driver.find_element_by_xpath(".//button[@data-toggle='dropdown']") ### XPATH = .//button[@data-toggle='dropdown']
select_dropdown.click()

#select_option = driver.find_element_by_
select_option.click()

#select.find_element_by_link_text('EUW')

search = driver.find_element_by_name("name")
search.send_keys("ArtourBabaevsky")
search.send_keys(Keys.RETURN)
#search.submit()  """

time.sleep(5) # Let the user actually see something!

driver.quit() 