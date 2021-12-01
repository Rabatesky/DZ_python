file = input()
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
i = file.rfind('.')
for f in extensions:
    if f == file[i+1:]:
        print(f)
        k = 1;
        break
if k != 1:                               # если нужны определённые расширения
    print("Такого расширения не существует, првоерьте правильность ввода")
#extensions.append(file[i+1:])            #если мы уверены в пользователе то добавляем новое расширение
#print(file[i+1:])