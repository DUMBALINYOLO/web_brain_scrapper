import os
import pathlib



def create_file(node):
    new_dir = pathlib.Path(os.getcwd(), node)
    new_dir.mkdir(parents=True, exist_ok=True)
    # You have to make a file inside the new directory
    new_file = new_dir / f'{node}.txt'
    new_file.write_text(node)
    
    return new_file


