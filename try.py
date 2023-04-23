#!/usr/bin/python3
import glob
import os

list_of_files = glob.glob('/versions/*.tgz') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)
