def word_count(phrase):
    phrase = phrase.split()
    for i in phrase:
        print(i)
    print('количество слов = ', len(phrase))
word_count("Тут фраза с пробелами и я хочу их распечатать по одному на строку и ещё посчитать слова")