sec=int(input())
day = sec // (60*60*24)
hour = (sec - day*60*60*24)//(60*60)
min = (sec - day*60*60*24 - hour*60*60) // 60
sec = (sec - day*60*60*24 - hour*60*60 - min*60) % 60
print(day, ':', hour, ':', min, ':', sec)