from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# Specify the path to the ChromeDriver executable executable_path='path/to/chromedriver'
driver = webdriver.Chrome()
# Open a webpage
driver.get('https://www.ah.nl/')
time.sleep(5)

driver.maximize_window()
time.sleep(10)

# Cancel cookies / Alles afwijzen
driver.find_element(By.ID, value="decline-cookies").click()
time.sleep(5)

# Inloggen mouse hover
inloggen = driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div[2]/nav/div[2]/menu/li[2]/button")
actions = ActionChains(driver)
actions.move_to_element(inloggen).perform()

time.sleep(10)

dropdown_inloggen = driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div[2]/nav/div[2]/menu/li[2]/div/menu/li[7]/button")
dropdown_inloggen.click()

time.sleep(5)

# username
username = driver.find_element(By.ID,value="username")
username.send_keys("example0001@yahoo.com")
time.sleep(2)

# password
password = driver.find_element(By.ID,value="password")
password.send_keys("Wachtwoord10*")
time.sleep(2)

# Login || Inloggen
login = driver.find_element(By.ID,value="login")
login.click()
time.sleep(2)

# Close the browser
driver.quit()