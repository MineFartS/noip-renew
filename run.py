from __init__ import args, keys, driver
from philh_myftp_biz.time import sleep
from philh_myftp_biz.web import get

# ==================================================================
# LOGIN

driver.open("https://www.noip.com/login")

# Get Username and Password from keyring
email = keys['email'].read()
password = keys['password'].read()

# Enter the username
driver.element('id', 'username')[0].send_keys(email)

# Enter the password
driver.element('id', 'password')[0].send_keys(password)

# Submit Form
driver.element('id', 'clogs-captcha-button')[0].click()

# ==================================================================
# 2-FACTOR AUTHENTICATION

# Check if 2FA is required
if (len(driver.element('ID', "firstInput", False)) > 0):
    
    # Wait for code to deliver to inbox
    sleep(3)

    # Get Script URL from keyring
    url = keys['Script URL'].read()

    # Get the 2FA code from the Script URL
    code = get(url = url).text.strip()

    # Enter 2FA code
    driver.element('ID', "firstInput")[0].send_keys(code)

# ==================================================================

driver.open("https://my.noip.com/dynamic-dns")

# Click 'Confirm'
driver.element(
    'xpath',
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[3]/div/div[2]/a'
)[0].click()

# Refresh the page
driver.reload()

# TODO (Bypass reCaptcha)

# ==================================================================
