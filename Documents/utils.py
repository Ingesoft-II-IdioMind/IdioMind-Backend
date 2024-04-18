from idiomind.settings import API_KEY
import google.generativeai as genai
import json

def translate_word(word, language, sentence=None):

    genai.configure(api_key=API_KEY)
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
