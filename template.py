import os
from pathlib import Path

files = []

# Loop through each file in the list
for file in files:
    # Create a Path object from the file path
    file_path = Path(file)
    
    # Get the directory name of the file (without the file name itself)
    dirname = file_path.parent
    
    # Make sure the directory exists
    os.makedirs(dirname, exist_ok=True)
    
    # Create an empty file if it doesn't exist
    file_path.touch(exist_ok=True)
