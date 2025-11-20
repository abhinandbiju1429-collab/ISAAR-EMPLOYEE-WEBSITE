import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Automatically download & use the correct ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))