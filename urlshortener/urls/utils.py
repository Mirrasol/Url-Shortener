import binascii
import hashlib
import os
import random


def get_hash(url):
    """
    Create a hash for a given URL.
    """
    salt = binascii.hexlify(data=os.urandom(5)).decode()
    url += salt
    url_hash = hashlib.md5(url.encode('UTF-8')).hexdigest()
    hash = ''
    for i in range(random.randint(5, 10)):
        hash += url_hash[random.randint(0, len(url_hash) - 1)]
    return hash
