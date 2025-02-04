# This code is unfinished
from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://www.noip.com/login")
browser.find_element(By.ID,"username").send_keys(email)
with open("pass.txt", "r") as pw:
    browser.find_element(By.ID,"password").send_keys(pw.readline().lstrip().rstrip())
browser.find_element(By.ID,"clogs-captcha-button").click()

try:
    time.sleep(10)
    browser.find_element(By.ID, "firstInput").send_keys( requests.get(Script_URL).text.split('\\x26')[1] )
    browser.find_element(By.NAME, "submit").click()
except:
    print('OTP Failed')
browser.get("https://my.noip.com/dynamic-dns")
#browser.find_element(By.NAME, "submit").click()
