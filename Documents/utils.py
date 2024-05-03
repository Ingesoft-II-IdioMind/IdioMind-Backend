from idiomind import settings
from firebase_admin import storage
import json
import requests
import fitz
import tempfile
from PIL import Image
from firebase_admin import storage

def translate_word(word, language, sentence=None):
    api_key=settings.API_KEY
    

    if sentence:
        prompt = "You are an assistant providing responses in JSON format. Provide the definition, description in its context, and three examples of the word " + word + " and its use in the following sentence: '" + sentence + "'. Follow this JSON format: {\"translation\":\"<your word translation to" + language + ">\", \"definition\":\"<definition in the original language>\", \"description\":\"<description in the original language>\", \"examples\":[\"<Example1>\",\"<Example2>\",\"<Example3>\"]}. Your responses (except the translation) must be in the language of the word " + word + "."
    else:
        prompt = "You are an assistant providing responses in JSON format. Provide the definition and three examples of the word " + word + ". Follow this JSON format: {\"translation\":\"<your word translation to" + language + ">\", \"definition\":\"<definition in the original language>\", \"examples\":[\"<Example1>\",\"<Example2>\",\"<Example3>\"]}. Your responses (except the translation) must be in the language of the word " + word + "."

    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }
    
    response = requests.post(endpoint, headers=headers, params={"key": api_key}, json=data)
    json_content = response.json()

    # Extracting information from the response
    result = json_content.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', None)
    result_dict = json.loads(result)
    translation = result_dict.get('translation')
    definition = result_dict.get('definition')
    examples = result_dict.get('examples')
    return translation,definition, examples


def subir_pdf(pdf_file,mail):
    try:
       
        bucket_name = settings.bucket_name
        bucket = storage.bucket(bucket_name)
        img = pdf_to_png(pdf_file)
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        img.save(temp_file.name)
        pdf_name = pdf_file.name
        existing_files = [blob.name for blob in bucket.list_blobs(prefix="Documents/")]
        existing_pdfs = [file for file in existing_files if file.endswith(pdf_name)]
        if existing_pdfs:
            pdf_name_parts = pdf_name.split(".")
            base_name = ".".join(pdf_name_parts[:-1])
            extension = pdf_name_parts[-1]
            counter = 1
            new_pdf_name = f"{base_name}_{mail}_{counter}.{extension}"
            while "Documents/" + new_pdf_name in existing_files:
                counter += 1
                new_pdf_name = f"{base_name}_{mail}_{counter}.{extension}"
        else:
            new_pdf_name = f"{pdf_name[:-4]}_{mail}_1"
        blob = bucket.blob("Documents/" + new_pdf_name + ".pdf")      
        blobportada = bucket.blob("images/" + new_pdf_name + ".png")     
        blob.upload_from_file(pdf_file, rewind=True)
        blobportada.upload_from_file(temp_file, rewind=True)

        blob.make_public()   
        blobportada.make_public()      
        # Devuelve la URL de descarga del archivo recién subido
        return blob.public_url, blobportada.public_url
    except Exception as e:
        print(f"Error al subir el archivo PDF a Firebase Storage: {e}")
        return None


def pdf_to_png(pdf_file):
    # Abrir el PDF y obtener el pixmap de la primera página
    pdf = fitz.open(stream=pdf_file.read())
    page = pdf.load_page(0)
    pix = page.get_pixmap()

    # Convertir el pixmap a una imagen PIL
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    return img