import model_print as mk_pr
import model_make_entry as mk_en


def edit_record(book):
    flag = False
    if input("Do you know the name, who you wanna edit?(y/n) ").lower() == "n":
        mk_pr.print_names(book)
    name, s = input("Put the name?"), None
    for k, v in book.items():
        if k == name:
            flag = True
            mk_pr.print_values(book, k)
            name = input(
                "What data you wanna edit?('0': delete , '1' : 'name', '2':'phone' , '3':'birthday' , '4':'email') ")
            if name == '1':
                book[k] = mk_en.write_birthday()
            elif name == '2':
                i = 0
                for j in book[k]['phone']:
                    print(i+1, j)
                    i += 1
                s = input("for deleting put order number, for add new type 'new' \n-").lower()
                if  s == 'new':
                    book[k]['phone']+=(mk_en.write_phone())
                elif int(s)<=i:
                    f=book[k]['phone'].pop(int(s)-1)
                    print(f"phone {f} is deleted in {k}")
                else:
                    print("Wrong entry")
                    break
            elif name == '3':
                book[k]['birthday'] =mk_en.write_birthday()
            elif name == '4':
                book[k]['email'] = input('put email - ')
            elif name == '0':
                s = k
                break
    if flag == False:
        print("No any record with such name!")
    if name == '0':
        del book[k]
        print(f"Record {k} is deleted \n")
