import streamlit as st
from streamlit_chat import message
from PIL import Image
from chatplm.model import ChatPLM

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
        st.markdown("<h1>ChatPLM</h1>", unsafe_allow_html=True)
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

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i],
                        is_user=True, key=str(i) + '_user')
                message(st.session_state["generated"][i], key=str(i))
                feedback = st.markdown(
                    "Something's wrong? <a href=#>Give feedback.</a>", unsafe_allow_html=True)
