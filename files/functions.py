FILENAME = "list"


def list_r(x_lc=FILENAME):
    """Return the elements of list.txt, or any other (textfile).txt (x_lc) in the files folder"""
    with open(f"files/{x_lc}.txt", 'r') as file_lc:
        todos_lc = file_lc.readlines()
    return todos_lc


def todos_w(todos):
    with open('files/list.txt', 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("Hello from functions")
