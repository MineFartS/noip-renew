from __init__ import keys

for key in keys:

    value = input(key + ' = ').strip()
    
    keys[key].save(value)
