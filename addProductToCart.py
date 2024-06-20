from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#path to the ChromeDriver
driver = webdriver.Chrome()
# Open a webpage
driver.get('https://www.ah.nl/')
time.sleep(5)

driver.maximize_window()
time.sleep(10)

# Cancel cookies / Alles afwijzen
driver.find_element(By.ID, value="decline-cookies").click()
time.sleep(5)

#click products page || Producten
driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div[2]/nav/menu/li[1]/a").click()
time.sleep(5)

# click on any product type || Bakkerij
driver.find_element(By.XPATH,"//*[@id='start-of-content']/div[1]/div/div/div/div[7]/div/a").click()
time.sleep(5)

# a new page should be opened || Brood
productType = driver.find_element(By.ID,value="svg-sprite")
productType.click()
time.sleep(5)

# Product || Bruin Brood
category = driver.find_element(By.XPATH,"//*[@id='start-of-content']/ul[1]/li[2]/a")
category.click()
time.sleep(5)

# Bakkersbrood bruin
subcategory = driver.find_element(By.XPATH,"//*[@id='start-of-content']/ul/li[3]/a")
subcategory.click()
time.sleep(5)

# product adding to the cart
productPlusButton=driver.find_element(By.XPATH,"//*[@id='446411485692568824568825168181230797231535']/article[1]/div[2]/div[1]/div/div/div[1]/button[3]")
productPlusButton.click()
time.sleep(5)

# view shopping cart
cart = driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div[2]/nav/div[2]/div/div/a")
cart.click()
time.sleep(7)

# Close the browser
driver.quit()


