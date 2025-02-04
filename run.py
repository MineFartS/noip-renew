from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import time

with open("logins.txt", "r") as logindata:
    Script_URL, email, password =  logindata.readlines()
    
    browser = webdriver.Firefox()
    browser.get("https://www.noip.com/login")

    # Enter No-IP Username and Password
    browser.find_element(By.ID,"username").send_keys(email.strip())
    browser.find_element(By.ID,"password").send_keys(password.strip())
    browser.find_element(By.ID,"clogs-captcha-button").click()

try:
    # Fetch No-IP 2FA Code From Google Apps Script API
    time.sleep(10)
    browser.find_element(By.ID, "firstInput").send_keys( requests.get(Script_URL.strip()).text.split('\\x26')[1] )
    browser.find_element(By.NAME, "submit").click()
except:
    print('OTP Failed')
browser.get("https://my.noip.com/dynamic-dns")
#browser.find_element(By.NAME, "submit").click()
