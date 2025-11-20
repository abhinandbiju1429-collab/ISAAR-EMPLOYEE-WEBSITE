#perform employee creation and deletion in the admin page 

import time
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
driver.find_element(By.XPATH,"//*[@id='root']/div/div/input").send_keys("Admin1122")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/input").send_keys("Isar@2025")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/input").send_keys("Admin1122")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/input").send_keys("Isar@2025")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
# Wait for dashboard (you can update the XPath based on your dashboard layout)
wait = WebDriverWait(driver, 100)
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[1]")))
print("✅ Dashboard loaded successfully!")
time.sleep(10)


driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
time.sleep(2)
print("clicked")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[4]/input[1]").send_keys("tester12")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[4]/input[2]").send_keys("ISARED00")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[4]/input[3]").send_keys("tester0000@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[4]/input[4]").send_keys("0000000000")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[4]/input[5]").send_keys("tester1429")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[4]/input[6]").send_keys("IT")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[4]/button").click()
time.sleep(5)
print("created employee successfully!")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/ul/li[46]/strong")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/ul/li[46]/button[2]").click()
time.sleep(5)
print("deleted employee successfully!")
time.sleep(3)


driver.quit()