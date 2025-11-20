#perform all the functions in the admin page except the employee creation and deletion

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
# Example: Scroll down
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
time.sleep(2)
print("✅ scrolled down successfully!")

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(2)
print("✅ scrolled up successfully!")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[3]/input[1]").send_keys("ABHINAND B")
time.sleep(2)
print("✅ Name  passed")

driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[3]/button").click()
time.sleep(5)
print("export csv successfully!")

#driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[3]/input[2]").send_keys("16-10-2025")
#time.sleep(2)
#driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[4]/table/tbody/tr[1]/td[6]/button").click()
#print("✅ clicked the photo ")
# Save the current window handle
#windowIDs = driver.current_window_handle

# Wait until a new window is opened
 #wait.until(EC.new_window_is_opened([windowIDs]))

# Get all open windows
##all_windows = driver.window_handles

# Identify the newly opened window
#for handle in all_windows:
#    if handle != windowIDs:
 #       new_window = handle
  #      break

# Switch to the new window
#driver.switch_to.window(new_window)
#print("✅ Switched to new window:", driver.title)

# Keep the new window open for 5 seconds
#time.sleep(5)

# Close the new window
#driver.close()
#print("❌ Closed the new window")

# Switch back to the original window
#driver.switch_to.window(windowIDs)
#print("🔙 Switched back to main window")
#time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='root']/nav/ul/li[2]/button").click()
print("✅ clicked the employee profile ")
time.sleep(1)
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/div[1]/input")))
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/input").send_keys("abhinand b")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='root']/nav/ul/li[3]/button").click()
print("✅ clicked the settings ")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='root']/nav/ul/li[4]/button").click()
print("✅ clicked punch correction")

# loop through option indexes 1–4 (depending on how many you have)
for i in range(1, 5):
    # open the dropdown
    driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/select").click()

    # click the i-th option
    option_xpath = f"//*[@id='root']/div/div/div/select/option[{i}]"
    driver.find_element(By.XPATH, option_xpath).click()
    print(f"✅ Selected option {i}")

    time.sleep(3)
driver.find_element(By.XPATH, " // *[ @ id = 'root'] / div / div / div / input").send_keys("abhinand b")
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='root']/nav/ul/li[5]/button").click()
time.sleep(2)
print(" clicked leave management")
# Locate the dropdown element
dropdown_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/select")

# Create a Select object
status_dropdown = Select(dropdown_element)

# List of options to select
options = ["All Status", "Pending", "Approved", "Rejected"]

# Loop through and select each option with delay
for option in options:
    status_dropdown.select_by_visible_text(option)
    print(f"✅ Selected: {option}")
    time.sleep(2)

time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='root']/nav/ul/li[6]/button").click()
time.sleep(5)
print("✅clicked task overview")

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
time.sleep(5)
print("✅ scrolled down successfully!")

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(3)
print("✅ scrolled up successfully!")

driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/input").send_keys("abhinand b")
time.sleep(2)

try:
    # Click on Analytics button
    driver.find_element(By.XPATH, "//*[@id='root']/nav/ul/li[7]/button").click()
    print("🖱️ Clicked Analytics button")

    # Wait for up to 65 seconds for the h3 element to appear
    wait = WebDriverWait(driver, 65)
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div/h3")))
    print("✅ Analytics page loaded")

    # Wait a bit before typing
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/input").send_keys("abhinand b")
    print("⌨️ Entered text in search box")

except TimeoutException:
    print("⚠️ Timeout: Page did not load within 65 seconds. Skipping to next step...")
except NoSuchElementException as e:
    print(f"⚠️ Element not found: {e}. Skipping to next step...")
except Exception as e:
    print(f"❌ Unexpected error: {e}. Skipping to next step...")

# Continue with the rest of your automation here
time.sleep(2)
print("➡️ Continuing with next steps...")

driver.find_element(By.XPATH, "//*[@id='root']/nav/ul/li[8]/button").click()
time.sleep(2)
print("clicked attendance summary")

# Locate the dropdown element
dropdown_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/select")

# Create a Select object
months = Select(dropdown_element)

# List of months to select
month_list = ["July 2025", "August 2025", "September 2025", "October 2025"]

# Loop through and select each month
for month in month_list:
    months.select_by_visible_text(month)
    print(f"✅ Selected: {month}")
    time.sleep(2)  # wait for 2 seconds between selections

driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/input").send_keys("abhinand b")
time.sleep(2)
print("✅ name passed")
driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/button").click()
time.sleep(2)
print("✅ download csv successfully!")
driver.find_element(By.XPATH, "//*[@id='root']/nav/ul/li[9]/button").click()



print("✅ logout")
time.sleep(5)
driver.quit()
