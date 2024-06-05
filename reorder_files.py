import os
import shutil
from pathlib import Path

source_dir = "/Users/javier/Downloads/"
dest_dir = "/Users/javier/Downloads"

def move_data(source,dest):
    
    for filename in os.listdir(source):

        name, extension = os.path.splitext(filename)
        source_dir = os.path.join(source + filename)
        
        if extension == '.pdf':
            dest = "/Users/javier/Downloads/PDF"
            print(f'archivo pdf finded : {filename}')
            shutil.move(source_dir, dest)

        elif extension in ['.jpeg', '.jpg', '.png', '.webp']:
            dest = "/Users/javier/Downloads/IMAGES"
            shutil.move(source_dir, dest)

        elif extension in ['.docx', '.doc']:
            dest = "/Users/javier/Downloads//WORD"
            shutil.move(source_dir, dest)
        elif extension in ['.xlsx', '.xls']:
            dest = "/Users/javier/Downloads//EXCEL"
            shutil.move(source_dir, dest)
        else:
            print('not type ')

move_data(source_dir, dest_dir)