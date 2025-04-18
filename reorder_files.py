import os
import shutil
from pathlib import Path

source_dir = "/Users/javier/Downloads/"
dest_dir = "/Users/javier/Downloads"

def move_files(source_dir, dest):
        try:
            shutil.move(source_dir, dest)
        except FileNotFoundError:
            print(f"File not found: {source_dir}")
        except PermissionError:
            print(f"Permission denied: {source_dir}")
        except Exception as e:
            print(f"Error moving file {source_dir}: {e}")
        except FileExistsError:
            print(f"File already exists: {source_dir}")

def move_data(source,dest):
    
    for filename in os.listdir(source):

        name, extension = os.path.splitext(filename)
        source_dir = os.path.join(source + filename)

        if extension == '':
            continue
        elif extension == '.pdf':
            dest = "/Users/javier/Downloads/PDF"
        elif extension in ['.jpeg', '.jpg', '.png', '.webp']:
            dest = "/Users/javier/Downloads/IMAGES"
        elif extension in ['.docx', '.doc', '.txt']:
            dest = "/Users/javier/Downloads/WORD"
        elif extension in ['.xlsx', '.xls']:
            dest = "/Users/javier/Downloads/EXCEL"
        else:
            dest = "/Users/javier/Downloads/OTHER"

        move_files(source_dir, dest)
        

        
if __name__ == "__main__":
    move_data(source_dir, dest_dir)