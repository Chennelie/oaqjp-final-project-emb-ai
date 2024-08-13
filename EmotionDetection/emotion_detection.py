import requests
import json

def emotion_detector(text_to_analyze) :
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputJson = { "raw_document": { "text": text_to_analyze } }

    # POST request to the url
    response = requests.post(url, json = inputJson, headers=header)

    # Format the response to get the good output format
    formatted_response = json.loads(response.text)

    # Extract the emotions from the output
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # Calculate the dominant emotion
    emotionsDict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotionsDict, key=emotionsDict.get)
    emotionsDict['dominant_emotion'] = dominant_emotion
            
    return emotionsDict