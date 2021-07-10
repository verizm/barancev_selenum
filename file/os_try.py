import os


# abs = os.path.abspath("../file/os_try.py")
# print(abs)
#
# dir_name = os.path.dirname(abs)
# print(dir_name)
#
# dir_name = os.path.dirname(dir_name)
# print(dir_name)
#
# print(os.path.dirname("/"))


def check_root():
    path = os.path.abspath(__file__)
    while True:
        path_before = path
        print(f"{path}")
        path = os.path.dirname(path_before)

        if len(path_before) == len(path):
            break


check_root()
