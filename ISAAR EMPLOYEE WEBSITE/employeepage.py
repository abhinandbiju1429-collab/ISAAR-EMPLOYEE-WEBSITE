import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# Automatically download & use the correct ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
print("✅ Chrome launched successfully!")
driver.get("https://employee.isaar.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='root']/div/div/input").send_keys("ISARED025039")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/input").send_keys("1234")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/input").send_keys("ISARED025039")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/input").send_keys("1234")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
# Wait for dashboard (you can update the XPath based on your dashboard layout)
wait = WebDriverWait(driver, 100)
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[1]")))
print("✅ Dashboard loaded successfully!")
time.sleep(10)

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[3]/button[1]").click()
time.sleep(2)
print("clicked the attendance csv")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[3]/button[2]").click()
time.sleep(2)
print("clicked the leave csv")
driver.find_element(By.XPATH,"//*[@id='root']/nav/ul/li[2]/button").click()
time.sleep(2)
print("clicked the profile")

wait = WebDriverWait(driver, 10)
name1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div[3]/input")))
name1.clear()
name1.send_keys("ABHINAND B")
print("changed the name")

phone1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div/div[4]/input")))
phone1.clear()
phone1.send_keys("8138869329")
time.sleep(2)
print("changed the phone number")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
time.sleep(2)
print("clicked the savechanges")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[5]/button").click()
time.sleep(2)
print("clicked the change password form")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[5]/button").click()
time.sleep(2)
print("closed the change password form")

driver.find_element(By.XPATH,"//*[@id='root']/nav/ul/li[3]/button").click()
time.sleep(2)
print("closed the leave management")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/form/div[1]/input").send_keys("16-10-2025")
time.sleep(2)
print("enter the start date")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/form/div[2]/input").send_keys("18-10-2025")
time.sleep(2)
print("enter the end date")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/form/div[3]/input").send_keys("fever")
time.sleep(2)
print("closed the leave management")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/form/button").click()
time.sleep(2)
print("clicked the apply")

act=ActionChains(driver)
act.send_keys(Keys.ARROW_RIGHT)
act.perform()
#filter1=driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/input")
#filter1.clear()
#filter1.send_keys("2025-12")
#filter1.submit()
#time.sleep(5)
#print("filter the date1 ")

date_input = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/input")
date_input.click()
date_input.send_keys("10")
act.send_keys(Keys.ARROW_RIGHT)
act.perform()
date_input.send_keys("2025")
print("filter 1")

time.sleep(5)


# Locate the dropdown element
dropdown_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/select")

# Create a Select object
status_dropdown = Select(dropdown_element)

# List of options to select
options = [ "Pending", "Approved", "Rejected","All"]

# Loop through and select each option with delay
for option in options:
    status_dropdown.select_by_visible_text(option)
    print(f"✅ Selected: {option}")
    time.sleep(2)

time.sleep(1)

#dropdown_element1 = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/select")
#status_dropdown = Select(driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/select/option[1]"))
#time.sleep(2)
#print("select all option")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/table/tbody/tr/td[6]/button").click()
time.sleep(3)
print("clicked the cancel")

driver.find_element(By.XPATH,"//*[@id='root']/nav/ul/li[4]/button").click()
time.sleep(3)
print("clicked the task tracking")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/form/input[1]").send_keys("TESTING")
time.sleep(3)
print("entered1")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/form/input[2]").send_keys("Testing ISAR EMS website")
time.sleep(3)
print("entered2")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/form/input[3]").send_keys("Admin page automation")
time.sleep(3)
print("entered3")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/form/button").click()
time.sleep(3)
print("clicked the add task")



# Locate the dropdown element
dropdown_element3 = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/table/tbody/tr[1]/td[4]/select")

# Create a Select object
status_dropdown3 = Select(dropdown_element3)

# List of options to select
options = [ "Pending", "In Progress", "Completed"]

# Loop through and select each option with delay
for option in options:
    status_dropdown3.select_by_visible_text(option)
    print(f"✅ Selected: {option}")
    time.sleep(3)

time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='root']/nav/ul/li[5]/button").click()
time.sleep(3)
print("clicked the punch")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/input[1]").send_keys("29-10-2025")
time.sleep(2)
print("enter correction date")

time_input = driver.find_element(By.XPATH, "//*[@id='root']/div/div/input[2]")
time_input.click()
time_input.send_keys("09")
act.send_keys(Keys.ARROW_RIGHT)
act.perform()
time_input.send_keys("00")
print("enter time1")

time_input1 = driver.find_element(By.XPATH, "//*[@id='root']/div/div/input[3]")
time_input1.click()
time_input1.send_keys("05")
act.send_keys(Keys.ARROW_RIGHT)
act.perform()
time_input1.send_keys("00")
print("enter time2 ")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/textarea").send_keys("by mistake ")
time.sleep(2)
print("enter reason")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
time.sleep(2)
print(" submit")

driver.find_element(By.XPATH,"//*[@id='root']/nav/ul/li[6]/button").click()
time.sleep(5)
print(" logout")

driver.quit()