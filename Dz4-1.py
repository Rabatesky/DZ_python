f = open(r'C:\Users\Admin\Desktop\qwe.txt', 'r')
student = {}
s = 0
k = 0
for text in f:
    i = text.find('.')
    student[text[0:i+1]] = int(text[i+2])
    s = s + int(text[i+2])
    k +=1
f.close()
s = s/k
for i in student.keys():
    if student[i] < s:
        print(i, 'ученик учится хуже среднего')
    else:
        print(i, 'ученик учится не хуже среднего')

    