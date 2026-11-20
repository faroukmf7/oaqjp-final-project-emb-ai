import requests
import json

def emotion_detector(text):
    text_to_analyze = text
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json = data,headers = header)
    formatted_response= json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    emotions_d ={}
    dominant_emotion = max(emotions,key=emotions.get)
    emotions_d['dominant_emotion'] = dominant_emotion
    for key, value in emotions.items():
        emotions_d[key] = value
    return emotions_d