import os
from pathlib import Path

files = [
    'DeepFake/Components/__init__.py',
    'DeepFake/Components/Training.py',
    'DeepFake/Components/Modeling.py',
    'DeepFake/Components/Prediction.py',
    'DeepFake/Components/Preprocessing.py',
    'DeepFake/Components/Validation.py',
    'DeepFake/Components/Data_Ingestion.py',
    'DeepFake/Components/Data_Transform.py',
    'DeepFake/Pipelines/__init__.py',
    'DeepFake/Pipelines/Training.py',
    'DeepFake/Pipelines/Testing.py',
    'DeepFake/Pipelines/Prediction.py',
    'DeepFake/logging.py',
    'DeepFake/exception.py',
    'DeepFake/__init__.py',
    'DeepFake/Utils/__init__.py',
    'Artifacts',
    'Docs',
    'main.py'
]

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
