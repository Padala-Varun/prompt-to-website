import zipfile
import os
from io import BytesIO

def create_zip_from_files(folder_path="generated_sites"):
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w") as zip_file:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            zip_file.write(file_path, arcname=filename)
    buffer.seek(0)
    return buffer
