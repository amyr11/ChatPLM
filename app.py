import streamlit as st
from streamlit_chat import message
from PIL import Image
from chatplm.model import ChatPLM
from chatplm.helpers.load_data import load_data

st.set_page_config(page_title="ChatPLM", page_icon="🤖")


@st.cache(allow_output_mutation=True)
def load_model():
    print('loaded model')
    return ChatPLM()


model = load_model()

tab1, tab2 = st.tabs(["Chat", "README"])

with tab1:
    # Setting page title and header
    image = Image.open('assets/chatplm_logo.png')
    col1, col2 = st.columns([1, 4], gap='medium')
    with col1:
        st.image(image, width=150)
    with col2:
        st.markdown("# ChatPLM `preview`", unsafe_allow_html=True)
        st.markdown("<h5>Ask anything about our Pamantasan!</h5>",
                    unsafe_allow_html=True)

    # Initialise session state variables
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []

    clear_button = st.button("Clear Conversation", key="clear")

    # reset everything
    if clear_button:
        st.session_state['generated'] = []
        st.session_state['past'] = []

    # container for chat history
    response_container = st.container()
    # container for text box
    container = st.container()

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_area("Ask ChatPLM", key='input', height=10)
            submit_button = st.form_submit_button(label='Send', type='primary')

        if submit_button and user_input:
            output = model.response_from_model(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    st.markdown('<p style="color: grey">This version is still under development. The model might answer inaccurately because of limited training data. <a href=#>Become a volunteer!</a></p>', unsafe_allow_html=True)
    st.markdown(
        f'<p style="color: grey; font-size: 12px">Training data updated on {load_data()["date"]}</p>', unsafe_allow_html=True)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i],
                        is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))
                feedback = st.markdown(
                    "Something's wrong? <a href=#>Give feedback.</a>", unsafe_allow_html=True)

with tab2:
    st.write('# What is ChatPLM? 🤔')
    st.write(
        'ChatPLM is a chatbot trained on PLM data for university-specific information queries.')

    st.write('# How does ChatPLM work? 🛠')
    st.write('ChatPLM consists of a neural network trained on PLM-specific data to identify the patterns of user prompts and provide the appropriate response. Using NLP techniques, ChatPLM is able to understand the context of the user\'s prompts.')

    st.write('## Natural Language Processing (NLP) 🗣')
    st.write('Natural Language Processing (NLP) is a field of artificial intelligence that deals with the interaction between computers and humans using the natural language. It is a branch of artificial intelligence that has many important applications in the modern world. NLP is used in search engines, email filters, voice recognition software, and many other applications.')

    st.write('## What on 🌏 is a neural network? 🤖')
    st.write('A neural network is a machine learning model that is inspired by the human brain. It is composed of layers of neurons that are connected to each other. Each neuron is a mathematical function that takes in an input and produces an output. The output of one neuron is the input of another neuron. The output of the last layer is the output of the neural network.')
    st.image(
        'https://miro.medium.com/v2/resize:fit:1199/1*N8UXaiUKWurFLdmEhEHiWg.jpeg')

    st.write('## ChatPLM is not a generative AI ❗️')
    st.write('Unlike ChatGPT, ChatPLM is not a generative AI. It does not generate responses from scratch. Instead, it uses a pre-trained language model to select responses from saved data based on the user\'s input. This prevents hallucination and ensures that the responses are relevant to the user\'s input.')

    st.write('# Technology used 💻')
    st.write('ChatPLM is built using the following technologies:')

    techs = ["![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)",
             "![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)",
             "![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)"]

    st.markdown(" ".join(techs))

    st.write('# Github Repository 🔗')
    st.write('https://github.com/amyr11/ChatPLM')
