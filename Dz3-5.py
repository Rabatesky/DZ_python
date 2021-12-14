numbers=[1,4,5,5]
numbers1 = [0,1,2,3,4,5,6,7,8,9]
try:
    for i in numbers:
        numbers1.remove(i)
    print('все уникальны')
except:
    print('не все числа уникальны')