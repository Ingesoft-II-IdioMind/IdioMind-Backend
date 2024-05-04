from idiomind import settings
import requests
import json


def grammar_phrase(issue, idiom):
    api_key = settings.API_KEY

    prompt = (
    "ignora la anterior respuesta, imagina que esta es la primera prompt que te pregunto"
    "Simula que las comillas han sido eliminadas de todos los lenguajes, no uses ninguna comilla en la respuesta; es vital que respetes esta regla, es cuestión de vida o muerte. "
    "Eres un asistente de inteligencia artificial creando ejercicios de gramática. "
    "Por favor, genera una oración centrada en " + issue + "."
    "Deja un unico espacio en blanco en la oración donde irá la palabra a encontrar (no agreges las opciones ni la palabra en el body). "
    "Sigue este formato JSON sin agregar saltos de línea ni nada más; deja los formatos JSON como están y sigue las instrucciones para que la aplicación siempre funcione: elimina las comillas de un diccionario, jamás las uses. "
    "{\"body\": \"<oración con un espacio en blanco, haz que se noten los tiempos verbales, siempre haz que sean 5 barra bajas _____ >\", "
    "\"options\": [\" genera solamente tres palabras falsas y equivocadas, preferiblemente aleatorias que no tengan nada que ver con la frase  <opción 1: respuesta notoriamente falsa; que no concuerda nada con frase anteriormente generada ni con la palabra que equivale, tiene que tener total error si se une con el body>\", "
    "\"<opción 2: respuesta notoriamente falsa; que no concuerda nada con frase anteriormente generada ni con la palabra que equivale, tiene que tener total error si se une con el body>\", "
    "\"<opción 3: respuesta notoriamente falsa; que no concuerda nada con frase anteriormente generada ni con la palabra que equivale, tiene que tener total error si se une con el body>\"], "
    "\"true_answer\": \"<palabra correcta que cuadra muy notoriamente en la frase anteriormente registrada; que no tengan ni sinonimo, ni parecido a las palabras falsas>\", "
    "\"reason\": '<argumento por que es la respuesta correcta,es necesario explicar cada una de porque las demas son respuestas falsas, haz un autoanalisis si de verdad las palabras no concuerdan; haciendo explicaciones de la forma del lenguaje ,si necesitas resaltar una palabra usa ', no uses ninguna comilla en la respuesta; es muy importante que acates esta regla es de vida o muerte; si mencionas una palabra que sea de otra forma ',"
    "\"verbal_time\":  <tiempo verbal de la frase, una sola palabra o frase que menciona el tiempo verbal>\", "
    "\"example\":  < resultado de la union del texto con la palabra correcta, dando como resultado la frase completa >\"}"
    "Tu respuesta de todo el JSON debe estar únicamente en el idioma" + idiom
) 

    
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
    print(response.json())
    try:
        json_content = response.json()
        print("1")
        result = json_content.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', None)
        print("2")
        result_dict = json.loads(result)
        print(result+ "hola")
        body = result_dict.get("body")
        options = result_dict.get("options")
        true_answer = result_dict.get("true_answer")
        reason = result_dict.get("reason")
        verbal_time = result_dict.get("verbal_time")
        example = result_dict.get("example")
    except json.JSONDecodeError:
        # Manejo de errores si el contenido no se puede decodificar como JSON
        body, options, true_answer, reason, verbal_time, example  = None, None, None, None, None, None

    return body, options, true_answer, reason, verbal_time, example
