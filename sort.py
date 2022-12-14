import os
import pathlib

sorter_file_name = os.path.basename(__file__)
root = os.getcwd() + "/example_folder/"

images = ['jpg', 'png', 'gif', 'jpeg']
video = ['mp4', 'mov', 'wmv', 'flv', 'avi']
doc = ['doc', 'docx', 'pdf']
sheet = ['xls', 'xlsx']
install = ['exe']
compressed = ['zip', 'rar']
text = ['txt']

def getFolderNameByExtension(extension):
     if extension in images:
          return "Images"
     elif extension in video:
          return "Videos"
     elif extension in doc:
          return "Documents"
     elif extension in sheet:
          return "Sheets"
     elif extension in install:
          return "Installables"
     elif extension in compressed:
          return "Compressed"
     elif extension in text:
          return "Text"
     else:
          return "Unknown"


for entry in os.scandir(root):
     if (entry.name == sorter_file_name):
          continue

     if entry.is_dir():
          typ = 'dir'
     elif entry.is_file():
          file_extension = pathlib.Path(entry.name).suffix
          file_extension = file_extension.split('.')[1]
          folder = getFolderNameByExtension(file_extension)
          path = root + folder
          is_exists = os.path.exists(path)
          if not is_exists:
               os.mkdir(path)
          os.rename(entry.path, path + '/' + entry.name)
     elif entry.is_symlink():
          typ = 'link'
     else:
          typ = 'unknown'
