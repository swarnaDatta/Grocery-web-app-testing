#import var
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Specify the path to the ChromeDriver executable executable_path='path/to/chromedriver'
driver = webdriver.Chrome()
# Open a webpage
driver.get('https://www.ah.nl/')
time.sleep(5)

driver.maximize_window()
time.sleep(10)

# Print the title of the webpage
print(driver.title)

# Cancel cookies / Alles afwijzen
driver.find_element(By.ID, value="decline-cookies").click()
time.sleep(5)

# Accept cookies / Alles accepteren
# driver.find_element(By.ID, value="accept-cookies").click()

# Inloggen mouse hover
inloggen = driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div[2]/nav/div[2]/menu/li[2]/button")
actions = ActionChains(driver)
actions.move_to_element(inloggen).perform()

time.sleep(10)

dropdown_inloggen = driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div[2]/nav/div[2]/menu/li[2]/div/menu/li[7]/button")
dropdown_inloggen.click()

time.sleep(5)

# Make a profile now // Maak nu een profiel aan
make_profile = driver.find_element(By.ID, value="link-create-account")
make_profile.click()
time.sleep(5)

# Nee, maak een nieuwe bonuskaart aan
make_new_bonus_card = driver.find_element(By.XPATH,"//*[@id='app']/div/div/main/div/div/div/div/main/div/div/div[2]/div/button[1]")
make_new_bonus_card.click()
time.sleep(5)

# click radio button // Bonuskaart + Mijn Albert Heijn
mijn_albert_heijn = driver.find_element(By.XPATH,"//*[@id='app']/div/div/main/div/div/div/div/main/div/div/div[2]/form/div/div/div[2]/div/div/div[1]/label")
mijn_albert_heijn.click()
print("button clicked")
time.sleep(5)

#scroll down
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
time.sleep(5)

# click Volgende
click_volgende = driver.find_element(By.XPATH,"//*[@id='app']/div/div/main/div/div/div/div/main/div/div/div[2]/form/div/div/div[3]/button")
click_volgende.click()
time.sleep(5)

# Inloggegevens
email_input = driver.find_element(By.ID, value="input-emailAddress")
email_input.send_keys('example0001@yahoo.com')
time.sleep(2)

#password
password = driver.find_element(By.ID, value="input-original")
password.send_keys('Wachtwoord10*')
time.sleep(2)

#repeat password
password_repeat = driver.find_element(By.ID, value="input-confirm")
password_repeat.send_keys('Wachtwoord10*')
time.sleep(2)

# radio gender // Aanhef
radio_gender_female = driver.find_element(By.XPATH,"//*[@id='app']/div/div/main/div/div/div/div/main/div/div/div/form/div[4]/div/div[2]/label")
radio_gender_female.click()
time.sleep(2)

# First name // Voornaam
first_name = driver.find_element(By.ID, value="input-first")
first_name.send_keys('abc')
time.sleep(2)

# Last name // Achternaam
last_name = driver.find_element(By.ID, value="input-last")
last_name.send_keys('def')
time.sleep(2)

# Date of birth // Geboortedatum
day = driver.find_element(By.ID, value="input-day")
day.send_keys('1')
time.sleep(2)

month = driver.find_element(By.ID, value="input-month")
month.send_keys('1')
time.sleep(2)

year = driver.find_element(By.ID,value='input-year')
year.send_keys('2000')
time.sleep(2)

# telephone number
telephone = driver.find_element(By.ID,value='input-phoneNumber')
telephone.send_keys('0612345678')
time.sleep(2)

# scroll down
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
time.sleep(5)

# Postcode
postcode = driver.find_element(By.ID,value="input-postalCode")
postcode.send_keys('1234AB')
print("Hello there!")
time.sleep(2)

# Huisnummer
huisnumber = driver.find_element(By.ID,value="input-houseNumber")
huisnumber.send_keys('100')
time.sleep(2)

# Submit // Meld je aan
submit = driver.find_element(By.XPATH,"//*[@id='app']/div/div/main/div/div/div/div/main/div/div/div/form/button")
submit.click()
time.sleep(5)

# Next page

# Data usage sharing dialog
# cancel
cancel = driver.find_element(By.XPATH,"//*[@id='data-usage-sharing-dialog']/footer/button[2]")
cancel.click()

# Finish
finish = driver.find_element(By.XPATH,"//*[@id='app']/div/div/main/div/div/div/button")
finish.click()

# Close the browser
driver.quit()
