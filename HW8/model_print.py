

def print_book(book):
    print("--------------------------")
    for k, v in book.items():
        print(k, " - ", end=" ")
        for i, j in v.items():
            print(i, j, end=" | ")
        print()
    print("-------------------------")

def print_names(book):
    i = 1
    for k in book.keys():
        print(i, "-", k)
        i+=1

def print_values(book, key):
    print(key, " - ", end=" ")
    for i, j in book[key].items():
        print(i, j, end=" | ")
    print()