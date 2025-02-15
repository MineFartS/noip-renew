from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import time

with open("logins.txt", "r") as logindata:
    Script_URL, email, password =  logindata.readlines()

    print('\n  ---  Connecting to browser session\n')

    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options, )

    browser.get("https://www.noip.com/login")

    print('\n  ---  Logging in with username and password from "Logins.txt"\n')

    # Enter No-IP Username and Password
    browser.find_element(By.ID,"username").send_keys(email.strip())
    browser.find_element(By.ID,"password").send_keys(password.strip())
    browser.find_element(By.ID,"clogs-captcha-button").click()

try:
    # Fetch No-IP 2FA Code From Google Apps Script API
    print('\n  ---  Fetching OTP Code ...\n')
    time.sleep(10)
    OTP_Code = requests.get(Script_URL.strip()).text.split('\\x26')[1]
    browser.find_element(By.ID, "firstInput").send_keys(OTP_Code)
    browser.find_element(By.NAME, "submit").click()
except:
    print('\n  ---  OTP Failed\n')
browser.get("https://my.noip.com/dynamic-dns")

print('\n  ---  Clicking Confirm\n')
browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr/td[6]/button[1]").click()

print('\n  ---  Closing browser session\n')

browser.close()
