
def checkEntry(entry, allowSymbols="", blockedSymbols=""):
    flag = True
    if len(allowSymbols) > 0:
        for i in entry:
            if i not in allowSymbols:
                print(f"Wrong symbol - {i}")
                flag = False
                return flag
    if len(blockedSymbols) > 0:
        for i in entry:
            if i in blockedSymbols:
                print(f"Wrong symbol {i}")
                flag = False
                return flag
    return flag


def checInt(entry, max, min=0, message=None):
    if entry > max:
        if message != None:
            print(message)
        print(f'{entry} more than max {max}')
        return False
    if entry < min:
        if message != None:
            print(message)
        print(f'{entry} less than min {min}')
        return False
    return True


def new_record(book):
    k = input("Put new name - ")
    a = {}
    a['phone'] = write_phone()
    a['birthday'] = write_birthday()
    a['email'] = "N/A"
    if input("put email?(y/n)").lower() == "y":
        a['email'] = input('put email - ')
    book[k] = a


def write_birthday():
    a = "N/A"
    if input("put bithday?(y/n)").lower() == "y":
        flag = False
        while flag == False:
            a = input('put birthday: DD.MM.YYYY - ')
            flag = checkEntry(a, ".0123456789")
            if len(a) != 10:
                print("Wrong amount of symbols")
                flag = False
                continue
            if len(a.split(".")) != 3:
                print("Wrong entry")
                flag = False
                continue
            for i, j, k in zip(list(map(int, a.split("."))), [31, 12, 9999], ["Wrong day", "Wrong month", "Wrong year"]):
                flag = checInt(entry=i, max=j, message=k)
                if flag == False:
                    break
    return a


def write_phone():
    flag = False
    while flag == False:
        a = list(
            input('put phone (separate phones by space bar ) - ').split())
        for i in a:
            flag = checkEntry(i, "+*#1234567890", )
            if flag == False:
                break
    return a
