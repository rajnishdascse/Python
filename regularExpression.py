import re
NameAge = '''
Janice is 22 and Theon is 33
Gabriel is 44 and Joey is 21
'''

age = re.findall(r'\d{1,3}',NameAge)    #d is for matches digit [0-9]
name = re.findall(r'[A-Z][a-z]*',NameAge)
ageDict = {}
x=0
for eachNames in name:
    ageDict[eachNames] = age[x]
    x +=1
print(ageDict)

"""
import re
if re.search('information','We would like to inform you that as per your information you have been selected'):
    print('There is a word like information')
"""