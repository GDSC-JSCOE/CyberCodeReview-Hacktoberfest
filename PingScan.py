pip install pyping  

import pyping
import csv


r = pyping.ping('google.com')

if r.ret_code == 0:
    print("Success")
else:
    print("Failed with {}".format(r.ret_code))
print("Congratulaions Ping Successful")
