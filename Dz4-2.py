f = open(r'C:\Users\Admin\Desktop\text.txt', 'r')
lec = 0
pract = 0
lab = 0
for text in f:
    i = text.find('лекц.')
    if i != -1:
        lec += 1
    i = text.find('лаб.')
    if i != -1:
        lab += 1
    i = text.find('практ.')
    if i != -1:
        pract += 1
print('Лекций:', lec)
print('Практических:', pract)
print('Лабораторных:', lab)