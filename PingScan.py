# Installing pyping 
pip install pyping  

# Imports
import pyping
import csv

r = pyping.ping('google.com')

if r.ret_code == 0: #if condition
    print("Success") 
else:
    print("Failed with {}".format(r.ret_code))
print("Congratulaions Ping Successful")
