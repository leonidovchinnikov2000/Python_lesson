from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/classattr')

sleep(10)
