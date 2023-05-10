a=[{6,'A'},(5,'R'),{2:'O'},{1:'C'},[3,'N'], {'hah,trick':{4:'G'}},7,'T',8,'U',9,'L',10,'A',{15:'S'},{14:'N'},{11:'T'},{12:'I'}]

new_a = []

for i, el in enumerate(a):
    if isinstance(el, set):
        int_val = None
        str_val = None

        for val in list(el):
            if isinstance(val, int): int_val = val
            else: str_val = val

        new_a.append((int_val, str_val))
    
    elif isinstance(el, list) or isinstance(el, tuple):
        new_a.append(el)

    elif isinstance(el, dict):
        item = list(el.items())[0]
        key = item[0]
        value = item[1]
        
        if isinstance(key, int):
            new_a.append((key, value))
        else:
            nested_item = list(value.items())[0]
            new_a.append((nested_item[0], nested_item[1]))

    elif isinstance(el, int):
        new_a.append((el, a[i+1]))

    else:
        pass


def get_word(list_letters):
    sorted_list_letters = sorted(list_letters, key=lambda x: x[0])

    print(sorted_list_letters)

    return "".join(list(map(lambda x: x[1], sorted_list_letters)))

word = get_word(new_a)
print(word)