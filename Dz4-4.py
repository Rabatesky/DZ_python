def str_max_len(text):
    maxlen = 0
    for i in text:
        if len(i) > maxlen:
            maxlen = len(i)
            word = i
    return word

def str_max_rep(text):
    count = {}
    max = 0
    for i in text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        if count[i] > max:
            max = count[i]
            word = i
    return word
f = open(r'C:\Users\Admin\Desktop\qwert.txt', 'r')
text = f.read()
text = text.lower()
text = text.replace("!", "")
text = text.replace("—", "")
text = text.replace("?", "")
text = text.replace(".", "")
text = text.replace(",", "")
text = text.split()
print(str_max_len(text))
print(str_max_rep(text))
    
    