from django.conf import settings
import cloudinary
from cloudinary.uploader import upload
import json
import requests
import fitz
import tempfile
from PIL import Image
from datetime import datetime
import os



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




def subir_pdf(pdf_file, mail):
    try:
        img = pdf_to_png(pdf_file)
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        img.save(temp_file.name)
        temp_file.seek(0)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename_without_extension = os.path.splitext(pdf_file.name)[0]
        unique_filename = f"{timestamp}_{mail}_{filename_without_extension}"
        pdf_file.seek(0)
        upload_pdf = cloudinary.uploader.upload(pdf_file, folder="Documents", public_id=unique_filename, resource_type="raw")
        upload_cover = cloudinary.uploader.upload( temp_file, folder="Images", public_id=unique_filename, resource_type="image")
        secure_url_pdf = upload_pdf["secure_url"]
        secure_url_cover =  upload_cover["secure_url"]
        
        # Devolver la URL del archivo PDF
        return secure_url_pdf,secure_url_cover
    except cloudinary.exceptions.Error as e:
        print(f"Error al subir el archivo PDF a Cloudinary: {e}")
        return None


def pdf_to_png(pdf_file):
    pdf = fitz.open(stream=pdf_file.read())
    page = pdf.load_page(0)
    pix = page.get_pixmap()
    # Convertir el pixmap a una imagen PIL
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    pdf_file.seek(0)
    return img