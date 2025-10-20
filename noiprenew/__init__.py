from philh_myftp_biz import web, time, db, pc

# ==================================================================

ring = db.Ring('noip-renew')

keys = {
    'Script URL': ring.Key('Script URL'),
    'email': ring.Key('email'),
    'password': ring.Key('password')
}

for n in keys:
    if keys[n].read() is None:
        v = input(n + ' = ').strip()
        keys[n].save(v)

pc.cls()

# ==================================================================

print('\n  ---  Connecting to browser session  ---\n')
b = web.browser(
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
    time.sleep(3)

    # Get Script URL from keyring
    url = keys['Script URL'].read()

    # Get the 2FA code from the Script URL
    code = web.get(url = url).text.strip()

    # Enter 2FA code
    b.element('ID', "firstInput")[0].send_keys(code)

# ==================================================================

b.open("https://my.noip.com/dynamic-dns")

print('\n  ---  Confirming Host  ---\n')

# TODO

# ==================================================================

print('\n  ---  Closing browser session  ---\n')
b.close()
