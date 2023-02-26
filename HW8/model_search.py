import model_print as mk_pr


def search_value(book):
    dic = {'0': "any", '1': 'name', '2': 'phone',
           '3': 'birthday', '4': 'email'}
    s = input(
        "Do you wanna search by:\n '0': any \n '1':'name'\n '2':'phone' \n '3':'birthday' \n '4':'email'\n- ")
    value = input("What to search? ")
    if s in "234":
        x = searchByColum(book, dic[s], value)
    elif s == "1":
        search_name(book, value)
    elif s == "0":
        search_any(book, value)


def searchByColum(book, colum, value, any="no"):
    flag = False
    for k in book.keys():
        j = book[k][colum]
        if isinstance(j, list):
            for _ in j:
                if value.lower() in _.lower():
                    print(f"'{value}' found in '{k}'",
                          " - ", colum, "-", _)
                    flag = True
                    return flag
        elif isinstance(j, str):
            if value.lower() in j.lower():
                print(f"'{value}' found in '{k}'", " - ", colum, "-", j)
                flag = True
                return flag
    if any == "no":
        if flag == False:
            print("Nothing found")
            return flag


def search_name(book, value):
    flag = False
    for k, v in book.items():
        if value.lower() in k.lower():
            mk_pr.print_values(book, k)
            flag = True
    if flag == False:
        print("Nothing found")


def search_any(book, word):
    flag = False
    for k, v in book.items():
        if word.lower() in k.lower():
            print(f"'{word}' found in name - '{k}'")
            mk_pr.print_values(book, k)
            if flag != True:flag = True
        for i in v.keys():
            tempBook = {}
            tempBook[k] = book[k]
            f = searchByColum(book=tempBook,colum= i,value= word, any="yes")
            if f == True: flag=f
    if flag == False:
        print("Nothing found")