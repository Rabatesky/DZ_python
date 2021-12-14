def print_overlord(mydict):
    for i in mydict.values():
        if isinstance(i, list):
            print_list(i)
        elif isinstance(i, dict):
            print_dict(i)
        else:
            print(i)

print_overlord(dict(key1=1,
            key2=[1, 2, 3, 4], 
            key3='Hello', 
            key4={"ciao":"Mondo", "Привет": "О дивный мир"}))