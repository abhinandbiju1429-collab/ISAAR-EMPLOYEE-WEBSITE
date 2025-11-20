import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service(r"C:\Users\admin\Desktop\abhi ml\msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)

driver.get("http://localhost:3000/employee-dashboard/profile")
driver.maximize_window()
time.sleep(5)
# Enter credentials



