import re

def namelist(names):
    if len(names) == 1:
        return names[0]["name"]
    elif len(names) == 0:
        return ''
    else:
        list = ""
        for name in names:
            list += f"{name['name']} "
        list = list.strip().replace(" ", ", ")
        lastComma = list.rfind(", ")
        ampersand = " &"
        list = list[:lastComma]+ampersand+list[lastComma+1:]
        return list


print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))