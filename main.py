def leet_speak(string:str) -> str:
    leet_dict = {
        '1': 'i',
        '3': 'e',
        '4': 'a',
        '5': 's',
        '7': 't',
        '0': 'o'
    }
    new_str = ''
    for i in string.lower():
        if i.isnumeric():
            string = string.replace(i,leet_dict.get(i, ''))
    return string

res = leet_speak('H3llo my name 28 is 3than and 1 10v3 34t1ng ph4d th41.')

print(res)

