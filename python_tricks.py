'''
#1)==========getting sorted dictionaries by the key value and sorted array element 
lis = [
    {'name' :'raj' , 'age': 21},
    {'name': 'riya', "age" : 19},
    {'name': 'tama', "age" : 23},
    
    ]
    
res = sorted(lis, key=lambda x : x['age'])
print(res)

#============sorted array============
res = [0,11,4,31,2,4,11,20]

print(sorted(res, reverse=True))

'''



#2)=============getting the sum of larger number using generator (declare in "("  
'''
import sys

lis = [ i for i in range(1000)]
print(sum(lis))
print(sys.getsizeof(lis), 'bytes')
print('---------------xxxxxx=---------------')
lis = ( i for i in range(1000))
print(sum(lis))
print(sys.getsizeof(lis), 'bits')
'''

#3)===============Getting the count using counter hashable function
'''
from collections import Counter
list_ = [1, 23, 10, 9, 1, 2, 33, 9, 1, 1, 21, 2, 2, 2, 3, 3, 3, 10, 21]

print(Counter(list_))
res = len(Counter(list_))
# print(res)
counter = Counter(list_)
counting_num = counter.most_common()
print(counting_num)
'''

'''
#4)===========.join method to add spance betweeen the strings

list_of_str = ['hi', 'this', 'is', 'Rajnish']
print(' '.join(list_of_str))
'''

#5)=========merging 2 dictionaries elements
'''

dict1 = {'name': 'rajnish', 'age': '21', 'bio':'bloody genius'}
dic2 = {'name': 'rajnish', 'id':1, 'location': 'india'}

merge = {**dict1,**dic2}
print(merge)

'''

'''

#6) ==== checking multiple condition/ or just one condition to fulfill

profile = 'engineering graduate'
location = 'indi'
age = 21

condition_check = [ profile== 'engineering graduate',
                    location =='india',
                    age==21]
if all(condition_check): #if all the condition satisfy it will run
    print('Candidate is eligible to apply')
    
#to consider anyone of the condition
if any(condition_check): #if any one of the condition satisfy then it will run
    print('Candidate is eligible')

'''

'''
#7)=================getting the most repeated number====

lists = [1,1,1,1,1,3,45, 9, 1,2,2,3,4,1,5, 53, 6, 3, 7]
# print(list(set(lists)))
most_repeat = max(set(lists), key = lists.count )
print(most_repeat)

'''

'''
#8)=============getting sum of number by entering multiple parameters at once

def get_sum(*a):
    res = 0
    for i in a:
        res += i
    print(res)

get_sum(2,3,4,5)  #and so on, you can put as much you wanna put
'''

#9) ======checking palindrome in just 2 lines

string = 'wow'
is_palindrome = string.find(string[::-1])==0
print(is_palindrome)














