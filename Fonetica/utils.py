import base64
from idiomind import settings
import requests
from gtts import gTTS
import json
from io import BytesIO
from langdetect import detect
import speech_recognition as sr
import tempfile
from pydub import AudioSegment

def speakingExamples(content):
    language = detect(content)
    print(language, "5")
    api_key = settings.API_KEY

    prompt = " forget the previous prompt, pretend that this is the first question. You are an  expert assistant providing responses in JSON format. Provide five example sentences where you use the string " + content + ". The examples must be in " + language + ". The response format must be: \"examples\":[\"<Example1>\",\"<Example2>\",\"<Example3>\"]}."

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
    print(json_content, "4")
    result = json_content.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', None)
    print(result, "3")
    # Parse the result as JSON and extract the "examples" list
    result_json = json.loads(result)
    print(result_json, "2")
    examples = result_json.get("examples", [])
    print(examples, "1")
    # Create a list of pronunciation audios
    pronunciation = []
    for example in examples:
        tts = gTTS(text=example, lang=language)
        audio_content = BytesIO()
        tts.write_to_fp(audio_content)
        audio_content.seek(0)
        audio_segment = AudioSegment.from_file(audio_content, format="mp3")
        wav_audio_content = BytesIO()
        audio_segment.export(wav_audio_content, format="wav")
        base64_audio = base64.b64encode(wav_audio_content.getvalue()).decode('utf-8')
        pronunciation.append(base64_audio)
    return result, pronunciation



def evaluate_pronunciation(audio_file_base64, target_sentence):
    # Decode base64 file
    audio_data = base64.b64decode(audio_file_base64)
    
    # Create a temporary audio file
    temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    temp_file.write(audio_data)
    temp_file.flush()

    # Initialize recognizer
    r = sr.Recognizer()

    # Detect language
    language = detect(target_sentence)

    # Load audio to memory
    with sr.AudioFile(temp_file.name) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language=language)

    # Split the transcribed text and target sentence into words
    transcribed_words = text.split()
    target_words = target_sentence.split()
    
    # Initialize lists to store correctly and incorrectly pronounced words
    correct_words = []
    incorrect_words = []

    # Compare each word in the transcribed text with the corresponding word in the target sentence
    for transcribed_word, target_word in zip(transcribed_words, target_words):
        if transcribed_word.lower() == target_word.lower():
            correct_words.append(target_word)
        else:
            incorrect_words.append(target_word)

    return correct_words, incorrect_words
