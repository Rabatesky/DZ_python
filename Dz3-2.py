print('введите имя файла')
file = input()
print('введите нужные расширения через пробел')
extensions = input()
extensions = extensions.split()
k = 0
i = file.rfind('.')
for f in extensions:
    if f == file[i+1:]:
        print(f)
        k = 1;
        break
if k != 1:
    print("Такого расширения не существует, првоерьте правильность ввода")