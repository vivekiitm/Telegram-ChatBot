import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import colorama 
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle

with open("intents.json") as file:
    data = json.load(file)


def chat(inp):
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                            truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])
    haveToDoGoogle = 1
    mx=0.0
    for i in range(len(result[0])):
        mx=max(mx,result[0][i])
    if(mx>=0.85):
        haveToDoGoogle=-1
    if(mx<=0.5):
        return "I dont know much about it", 1
    for i in data['intents']:
        if i['tag'] == tag:
            return np.random.choice(i['responses']), haveToDoGoogle


