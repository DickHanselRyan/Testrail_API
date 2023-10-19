##This is tutorial for Getting Case ID from Testrail using Automation
##Testrail API integration with automation
##This is project for Automation
##Tutorial only, not for real automation work-related
##All codes provided by supervisor with modification

# Import Modules
from testrail import *
import argparse
from pprint import *
import re

# Initialize Testrail Account
'''
NEVER SHARE YOUR USER ID AND PASSWORD ONTO PUBLIC!
'''
client = APIClient('https://inline.testrail.io/') #Insert your Testrail URL
client.user = '' #Insert your Testrail User ID
client.password = '' #Insert your Testrail Password


#Get all the test case id in a test run
test_id = client.send_get('get_tests/811')
# print(test_id)

# Show the keys on the dictionary
# pprint(test_id.keys())

#Remove keys from dictionary
rem_list = ['offset', 'limit', 'size', '_links']
for key in rem_list:
    del test_id[key]
# pprint(test_id)

# #Convert dict to str
test_id = str(test_id)


#Grab useful informations
ids = r"'case_id': (\d+)"
case = re.findall(ids, test_id)
# print(case)

case_id =[]
title = []
