FILENAME = "list"


def list_r(x_lc=FILENAME):
    """Return the elements of list.txt, or any other (textfile).txt (x_lc) in the files folder"""
    with open(f"files/{x_lc}.txt", 'r') as file_lc:
        todos_lc = file_lc.readlines()
    return todos_lc


def print_index(x_lc):
    """Enumerates the contents of x_lc, putting an index in front of the item: 1.First_Item"""
    for index_lc, item_lc in enumerate(x_lc):
        index_lc = int(index_lc) + 1
        item_lc = item_lc.capitalize().strip('\n')
        print(f"{index_lc}.{item_lc}")


def todos_w(x, z):
    with open('files/list.txt', 'w') as file_lc:
        x.remove(z)
        file_lc.writelines(x)


if __name__ == "__main__":
    print("Hello from functions")
