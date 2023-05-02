import pickle
import numpy as np
from tensorflow import keras
from chatplm.helpers.load_data import load_data


class ChatPLM:
    def __init__(self, intents_path, model_file, tokenizer_file, label_encoder_file):
        self.data = load_data(intents_path)
        # load trained model
        self.model = keras.models.load_model(model_file)

        # load tokenizer object
        with open(tokenizer_file, 'rb') as handle:
            self.tokenizer = pickle.load(handle)

        # load label encoder object
        with open(label_encoder_file, 'rb') as enc:
            self.lbl_encoder = pickle.load(enc)

    def response_from_model(self, inp):
        # parameters
        max_len = 20

        result = self.model.predict(keras.preprocessing.sequence.pad_sequences(
            self.tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
        tag = self.lbl_encoder.inverse_transform([np.argmax(result)])

        for i in self.data['intents']:
            if i['tag'] == tag:
                response = np.random.choice(i['responses'])
                return response
