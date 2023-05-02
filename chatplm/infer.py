import pickle
import json
import numpy as np
from tensorflow import keras


def response_from_model(inp, intent_file, model_file, tokenizer_file, label_encoder_file):
    with open(intent_file) as file:
        data = json.load(file)
    # load trained model
    model = keras.models.load_model(model_file)

    # load tokenizer object
    with open(tokenizer_file, 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open(label_encoder_file, 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20

    result = model.predict(keras.preprocessing.sequence.pad_sequences(
        tokenizer.texts_to_sequences([inp]), truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            response = np.random.choice(i['responses'])
            return response
