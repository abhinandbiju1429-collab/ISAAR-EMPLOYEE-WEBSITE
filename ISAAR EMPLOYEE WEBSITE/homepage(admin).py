import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Automatically download & use the correct ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
print("✅ Chrome launched successfully!")
driver.get("https://employee.isaar.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='root']/div/div/input").send_keys("Admin1122")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/input").send_keys("Isar@2025")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/input").send_keys("Admin1122")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/input").send_keys("Isar@2025")
driver.find_element(By.XPATH,"//*[@id='root']/div/div/button").click()
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[1]")))
print("✅ Dashboard loaded successfully!")
time.sleep(5)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
driver.execute_script("window.scrollTo(0,-document.body.scrollHeight);")
time.sleep(5)