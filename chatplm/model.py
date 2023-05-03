import os
import pickle
import numpy as np
from tensorflow import keras
from chatplm.helpers.load_data import load_data

# Get the directory of the current script
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(CURRENT_DIRECTORY, "chat_model")
TOKENIZER_FILE = os.path.join(CURRENT_DIRECTORY, "tokenizer.pickle")
LABEL_ENCODER_FILE = os.path.join(CURRENT_DIRECTORY, "label_encoder.pickle")


class ChatPLM:
    def __init__(self):
        self.data = load_data()
        # load trained model
        self.model = keras.models.load_model(MODEL_FILE)

        # load tokenizer object
        with open(TOKENIZER_FILE, 'rb') as handle:
            self.tokenizer = pickle.load(handle)

        # load label encoder object
        with open(LABEL_ENCODER_FILE, 'rb') as enc:
            self.lbl_encoder = pickle.load(enc)

    def response_from_model(self, inp):
        # parameters
        max_len = 20

        result = self.model.predict(keras.preprocessing.sequence.pad_sequences(
            self.tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
        tag = self.lbl_encoder.inverse_transform([np.argmax(result)])

        for i in self.data['intents']:
            if i['tag'] == tag:
                response = i['response']
                return response
