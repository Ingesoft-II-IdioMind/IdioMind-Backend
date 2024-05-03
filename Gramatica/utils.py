from idiomind import settings
import requests
import json


def grammar_phrase(issue,idiom):
    api_key=settings.API_KEY
    

 
    prompt = "You are an assistant providing exercises in grammar format. Please generate a sentence aimed at learning grammar. giving 4 options where only and strictly one word is correct, no other word can be valid in the text, " + issue + " with a blank space for the word.Follow this JSON format ever: {\"text\":\"<the body of the sentence that must be structured in detail, without containing the word>\", \"options\":[\"<four possible words that could go in the sentence where only one is correct and should not be repeated,Strictly only one can be correct>\"],\"true_answer\":\"<the correct answer corresponding to the phrase,The rest of the answers must be wrong.>\"}.Be careful with phrases that words in different tenses can have values ,Your response must be solely and exclusively in the " + idiom + "." 
   


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
    text = result_dict.get('text')
    options = result_dict.get('options')
    true_answer = result_dict.get('true_answer')
    return text,options,true_answer
