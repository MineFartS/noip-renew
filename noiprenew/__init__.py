from philh_myftp_biz.db import Ring, Key
from typing import Generator

# ==================================================================

ring = Ring('noip-renew')

keys = {
    'Script URL': ring.Key('Script URL'),
    'email': ring.Key('email'),
    'password': ring.Key('password')
}

# ==================================================================

def ask_input(only_blank:bool) -> Generator[bool, Key]:
    
    for n in keys:

        if (keys[n].read() != None) and only_blank:
            continue

        v = input(n + ' = ').strip()
        keys[n].save(v)
