import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# Open the website
driver.get("https://testautomationpractice.blogspot.com/")
print("✅ Page opened")

# Type 'selenium' into Wikipedia search box and click search
search_box = wait.until(EC.presence_of_element_located((By.ID, "Wikipedia1_wikipedia-search-input")))
search_box.send_keys("selenium")

search_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input")
))
search_button.click()
print("🔍 Search submitted")

# ✅ Wait until the search results are visible
wait.until(EC.visibility_of_element_located((By.ID, "wikipedia-search-result-link")))
print("✅ Search results are visible now")

# ✅ Wait until the specific link 'Selenium' is clickable
selenium_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Selenium")))
selenium_link.click()
print("✅ 'Selenium' link clicked")

# Click on other related links (if they exist)
other_links = ["Selenium in biology", "Selenium (software)", "Selenium disulfide", "Selenium dioxide"]

for text in other_links:
    try:
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, text)))
        element.click()
        print(f"✅ Clicked: {text}")
        time.sleep(1)
    except:
        print(f"⚠️ '{text}' not found — skipped")

# Switch through all tabs/windows and print titles
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print("🪟 Window title:", driver.title)

time.sleep(5)
driver.quit()
print("✅ Browser closed successfully")
