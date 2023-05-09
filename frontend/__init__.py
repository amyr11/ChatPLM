import streamlit.components.v1 as components

_component_func = components.declare_component(
    "feedback_buttons", path='./frontend')


def feedback_buttons(key):
    return _component_func(key=key, default=0)
