from .__init__ import ask_input, keys
from philh_myftp_biz.time import sleep
from philh_myftp_biz.web import browser, get
from philh_myftp_biz.pc import cls
from philh_myftp_biz import args

# ==================================================================

ask_input(only_blank=('reset' not in args()))

cls()

# ==================================================================

print('\n  ---  Connecting to browser session  ---\n')

b = browser(
    headless = False,
    debug = True
)

# ==================================================================

b.open("https://www.noip.com/login")

print('\n  ---  Logging in  ---\n')

# Get Username and Password from keyring
email = keys['email'].read()
password = keys['password'].read()

# Enter the username
b.element('id', 'username')[0].send_keys(email)

# Enter the password
b.element('id', 'password')[0].send_keys(password)

# Submit Form
b.element('id', 'clogs-captcha-button')[0].click()

# ==================================================================

# Check if 2FA is required
if (len(b.element('ID', "firstInput", False)) > 0):

    print('\n  ---  Fetching OTP Code  ---\n')
    
    # Wait for code to deliver to inbox
    sleep(3)

    # Get Script URL from keyring
    url = keys['Script URL'].read()

    # Get the 2FA code from the Script URL
    code = get(url = url).text.strip()

    # Enter 2FA code
    b.element('ID', "firstInput")[0].send_keys(code)

# ==================================================================

b.open("https://my.noip.com/dynamic-dns")

print('\n  ---  Confirming Host  ---\n')

# TODO

# ==================================================================

print('\n  ---  Closing browser session  ---\n')
b.close()
