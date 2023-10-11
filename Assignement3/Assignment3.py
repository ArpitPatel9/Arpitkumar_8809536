from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the primevideo.com homepage
driver.get("https://www.primevideo.com/")
time.sleep(2)

# Selecting a category
category_link = driver.find_element("xpath","/html/body/div[1]/div[1]/header/div[1]/div/div/div/div[1]/div/ol/li[4]/label/a")
category_link.click()
time.sleep(2)

# selecting Comedy category
comedy_link = driver.find_element("xpath","/html/body/div[1]/div[2]/main/div/div[2]/div[2]/h3[3]/a")
comedy_link.click()
time.sleep(2)

# Selecting a Movie
movie_link = driver.find_element("xpath","/html/body/div[1]/div[2]/main/div/div[3]/div/section/div/ul/li[1]/article/section/div/a")
movie_link.click()
time.sleep(2)

# Clicking on watch now button
watch_now = driver.find_element("xpath","/html/body/div[1]/div[1]/main/div[1]/div/div/div[2]/div[3]/div/div[2]/div[6]/div/div/div/div/div/div[2]/div/div[1]/a")
watch_now.click()
time.sleep(2)
# Closing the webdriver
driver.close()
