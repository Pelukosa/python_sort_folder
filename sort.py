import os
import pathlib

root = 'example_folder/'

for entry in os.scandir(root):
   if entry.is_dir():
        typ = 'dir'
   elif entry.is_file():
        typ = 'file'
        file_extension = pathlib.Path(entry.name).suffix
        path = root + file_extension.split('.')[1]
        is_exists = os.path.exists(path)
        if not is_exists:
            os.mkdir(path)
        os.rename(entry.path, path + '/' + entry.name)
   elif entry.is_symlink():
        typ = 'link'
   else:
        typ = 'unknown'
   print('{name} {typ}'.format(
        name=entry.name,
        typ=typ,
   ))