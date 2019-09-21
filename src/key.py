import sys
import hashlib

print(hashlib.sha224(sys.argv[0].encode('utf-8')).hexdigest())
