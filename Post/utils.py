from idiomind import settings
from firebase_admin import storage

def subir_image(image_file):
    try:
        bucket_name = settings.bucket_name
        bucket = storage.bucket(bucket_name)
        image_name = image_file.name
        
        # Obtener una lista de todos los archivos en el directorio "Post" en Firebase Storage
        blobs = list(bucket.list_blobs(prefix="Post/"))

        # Contar el número de archivos con el mismo nombre
        count = sum(1 for blob in blobs if blob.name.endswith(image_name))

        # Obtener la extensión de la imagen
        extension = image_name.split('.')[-1]

        # Generar un nuevo nombre de archivo único con la extensión adecuada
        new_image_name = f"{image_name.split('.')[0]}_{count + 1}.{extension}"
        
        # Subir el archivo con el nuevo nombre
        blob = bucket.blob("Post/" + new_image_name)
        blob.upload_from_file(image_file)
        blob.make_public()
        return blob.public_url
    except Exception as e:
        print(f"Error al subir el archivo de imagen a Firebase Storage: {e}")
        return None