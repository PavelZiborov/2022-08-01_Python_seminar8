# data [фамилия, имя, телефон, описание]
def search_last_name(name, data):
    for s in data:
        if name in s[0]:
            return s
    return None

def search_name(name, data):
    for s in data:
        if name in s[1]:
            return s
    return None

def search_tele(tel, data):
    for s in data:
        if tel in s[2]:
            return s
    return None