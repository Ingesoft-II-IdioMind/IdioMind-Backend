import base64
from idiomind import settings
import requests
from gtts import gTTS
import json
from io import BytesIO
from langdetect import detect

def speakingExamples(content):
    language = detect(content)
    print(language,"5")
    api_key=settings.API_KEY

    prompt = " forget the previous prompt, pretend that this is the first question. You are an  expert assistant providing responses in JSON format. Provide five example sentences where you use the string "  + content + ". The examples must be in "  + language + ". The response format must be: \"examples\":[\"<Example1>\",\"<Example2>\",\"<Example3>\"]}."

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
    print(json_content,"4")
    result = json_content.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', None)
    print(result,"3")
    # Parse the result as JSON and extract the "examples" list
    result_json = json.loads(result)
    print(result_json,"2")
    examples = result_json.get("examples", [])
    print(examples,"1")
    # Create a list of pronunciation audios
    pronunciation = []
    for example in examples:
        audio_content = BytesIO()
        tts = gTTS(text=example, lang=language)
        tts.write_to_fp(audio_content)
        audio_content.seek(0)
        base64_audio = base64.b64encode(audio_content.read()).decode('utf-8')
        pronunciation.append(base64_audio)
    return result, pronunciation