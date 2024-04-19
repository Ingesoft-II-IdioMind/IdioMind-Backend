from idiomind import settings
import google.generativeai as genai
from firebase_admin import storage
import json

def translate_word(word, language, sentence=None):
    genai.configure(api_key=settings.API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    if sentence:
        prompt = "You are an assistant providing responses in JSON format. Provide the definition, description in its context, and three examples of the word " + word + " and its use in the following sentence: '" + sentence + "'. Follow this JSON format: {\"translation\":\"<your word translation to" + language + ">\", \"definition\":\"<definition in the original language>\", \"description\":\"<description in the original language>\", \"examples\":[\"<Example1>\",\"<Example2>\",\"<Example3>\"]}. Your responses (except the translation) must be in the language of the word " + word + "."
    else:
        prompt = "You are an assistant providing responses in JSON format. Provide the definition and three examples of the word " + word + ". Follow this JSON format: {\"translation\":\"<your word translation to" + language + ">\", \"definition\":\"<definition in the original language>\", \"examples\":[\"<Example1>\",\"<Example2>\",\"<Example3>\"]}. Your responses (except the translation) must be in the language of the word " + word + "."
   
    response = model.generate_content(prompt)
    json_content = str(response.text)
    
    # Remove the markdown code block syntax (json and )
    json_content = json_content.replace('json\n', '').replace('\n', '')
    json_content = json.loads(json_content)
    
    # Asegurarse de que todos los campos estén presentes en el objeto JSON
    translation = json_content.get('translation', None)
    definition = json_content.get('definition', None)
    description = json_content.get('description', None)
    examples = json_content.get('examples', None)
    
    return {
        'translation': translation,
        'definition': definition,
        'description': description or 'None',  # Si no hay descripción, establecer en 'None'
        'examples': examples,
    }

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
