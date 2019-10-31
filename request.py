"""
Simple Web crawler by Vysakh Sreekumaran
Mail : letterstovysakh@gmail.com
"""

import requests
URL = raw_input("Enter URL ")
r = requests.get(URL)
f = open("Data.txt","w+")
f.write(r.content)
f.close
