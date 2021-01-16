#!/usr/bin/env python3

import requests
import gnupg
from datetime import datetime

# Set the URL that hosts your signing key.
url = ""

r = requests.get(url)

# Return our gpg key object to the working directory. Your "key.gpg" should reflect the actual key you are fetching.
with open('key.gpg', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):             
        fd.write(chunk)

# Initialize a 'home' for gpg per the docs, then scan the key.
gpg = gnupg.GPG(gnupghome='/home/user/.gnupg')

'''
The following method scans a given key and returns a dictionary.
We are most interested in the "expires" value, which python-gnupg retruns this as a
UNIX timestamp, so we need to convert that to check against what apt-key has.
'''

def will_expire_soon(key)
    key = gpg.scan_keys('aptly.gpg')

    timestamp = [timestamp['expires'] for timestamp in timestamp]
    
    # This returns an error in the REPL: "TypeError: an integer is required (got type list). Convert the dict value to integer.
    expires_on = datetime.fromtimestamp(timestamp)

    # Set current date and time to calcuate remaining time before key expiry
    curr_date = datetime.utcnow()

    if curr_date <= expires_on:
        pass


