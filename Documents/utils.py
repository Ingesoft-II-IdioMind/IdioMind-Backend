from idiomind import settings
from firebase_admin import storage
import json
import requests

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


def subir_pdf(pdf_file):
    try:
        bucket_name = settings.bucket_name
        # Obtén el nombre del bucket de almacenamiento desde la configuración
        # Obtén una referencia al archivo en Firebase Storage
        bucket = storage.bucket(bucket_name)
        blob = bucket.blob("Documents/" + pdf_file.name)      
        # Sube el archivo PDF al depósito de Firebase Storage
        blob.upload_from_file(pdf_file)   
        blob.make_public()         
        # Devuelve la URL de descarga del archivo recién subido
        return blob.public_url
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante la carga del archivo
        print(f"Error al subir el archivo PDF a Firebase Storage: {e}")
        return None
