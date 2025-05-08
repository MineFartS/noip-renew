try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import requests, time, os, requests
    from webdriver_manager.chrome import ChromeDriverManager
except:
    import subprocess, sys
    subprocess.call([sys.executable, '-m', 'pip', 'install', 'selenium', 'webdriver-manager'])
    subprocess.call([sys.executable, sys.argv[0]])
    exit()
# TODO Add Update Feature

os.chdir(os.getcwd())

Script_URL, email, password = open("Config.txt", "r").readlines()

print('\n  ---  Connecting to browser session  ---\n')
options = webdriver.ChromeOptions()

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.implicitly_wait(10)
browser.get("https://www.noip.com/login")

print('\n  ---  Logging in with username and password from "Config.txt"  ---\n')
# Enter No-IP Username and Password
browser.find_element(By.ID, "username").send_keys(email.strip())
browser.find_element(By.ID, "password").send_keys(password.strip())
browser.find_element(By.ID, "clogs-captcha-button").click()

try:
    # Fetch No-IP 2FA Code From Google Apps Script API
    print('\n  ---  Fetching OTP Code  ---\n')
    time.sleep(10)
    browser.find_element(By.ID, "firstInput").send_keys(requests.get(Script_URL.strip()).text)
    browser.find_element(By.NAME, "submit").click()
except:
    print('\n  ---  OTP Failed  ---\n')

time.sleep(2)
browser.get("https://my.noip.com/dynamic-dns")

print('\n  ---  Confirming Host  ---\n')
browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr/td[6]/button[1]").click()

time.sleep(2)
browser.refresh()

url = browser.current_url

browser.execute_script("""document.getElementsByClassName('col-md-6')[0].innerHTML = `<h3>MineFarts' NoIP Renewal Script<h3>
<a href="https://github.com/MineFartS/noip-renew">Open in Github</a>
</t1>Until this Script can bypass the captchas, you will need to solve them manually</t1>`""")

if browser.current_url == 'https://my.noip.com/dynamic-dns':
    browser.close()

while True:
    try: 
        if browser.current_url != url: break
    except: time.sleep(1)

print('\n  ---  Closing browser session  ---\n')
browser.close()
