import os
import pathlib

sorter_file_name = os.path.basename(__file__)
root = os.getcwd() + "/"

for entry in os.scandir(root):

    if entry.name == sorter_file_name:
        continue
    if entry.is_dir():
        typ = 'dir'
    elif entry.is_file():
        typ = 'file'
        file_extension = pathlib.Path(entry.name).suffix
        if file_extension != '':
            path = root + file_extension.split('.')[1]
            is_exists = os.path.exists(path)
            if not is_exists:
                print("Create folder: " + path)
                os.mkdir(path)
            os.rename(entry.path, path + '/' + entry.name)
            print("Moving: " + entry.path + ' - ' + path + '/' + entry.name)
    elif entry.is_symlink():
        typ = 'link'
    else:
        typ = 'unknown'
#    print('{name} {typ}'.format(
#         name=entry.name,
#         typ=typ,
#    ))
