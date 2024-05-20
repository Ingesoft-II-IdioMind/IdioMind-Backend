from idiomind import settings
from firebase_admin import storage
import cloudinary
from datetime import datetime
import os

def subir_image(image_file):
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename_without_extension = os.path.splitext(image_file.name)[0]
        unique_filename = f"{timestamp}_{filename_without_extension}"
        image_file.seek(0)
        upload_post = cloudinary.uploader.upload(image_file, folder="Post", public_id=unique_filename, resource_type="image")
        secure_url_post=  upload_post["secure_url"]     
        return secure_url_post
    except Exception as e:
        print(f"Error al subir el archivo de imagen a Firebase Storage: {e}")
        return None
    

 