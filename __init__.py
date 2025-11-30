from philh_myftp_biz.web import get, Driver
from philh_myftp_biz import ParsedArgs
from philh_myftp_biz.db import Ring

# ==================================================================

args = ParsedArgs()

# ==================================================================

ring = Ring('noip-renew')

keys = {
    'Script URL': ring.Key('Script URL'),
    'email': ring.Key('email'),
    'password': ring.Key('password')
}

# ==================================================================

driver = Driver(
    headless = (not args['verbose']),
    debug = args['verbose']
)

# ==================================================================