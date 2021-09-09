import random as rn

# print('Imported')
# for i in range(10):
#     print(rn.randint(1,9))

rn.seed(1)
print('Random Number : ',[rn.randint(0,9) for i in range(5)])    

# rn.seed(2)
print('Random Number : ',[rn.randint(0,9) for i in range(5)])    

# lst = ['R','W','Y','G','B','Black','P','O','I']
# print(len(lst))

# for i in range(len(lst)):
#     r = rn.randint(0,8)
#     print(lst[r])