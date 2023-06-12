import streamlit as st
from textwrap import TextWrapper
from reflect.constants import reflect_image_path, github_image_path, patreon_image_path
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title='Reflect', page_icon="⚫️", layout="wide", initial_sidebar_state='collapsed')
st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 14rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 14rem;}}
    </style>
''', unsafe_allow_html=True)

with st.sidebar:
    main_page = st.button('Reflect', use_container_width=1)
    about_page = st.button('About', use_container_width=1)
    if not about_page:
        main_page = True

if main_page:
    cola, colb = st.columns([2, 9])
    cola.markdown(
        f"""<a target="_self" href="{'https://reflect.streamlit.app/'}"><img src="{reflect_image_path}" style="display:block;" width="100%" height="100%"></a>""",
        unsafe_allow_html=1)
    colb.markdown('# Reflect \nAn AI group for prompt engineering')


if about_page:
    st.markdown('# About \n')
    st.write(
        "Built by [Erick Martinez](https://github.com/erickfm) using OpenAI, LangChain, and Streamlit"
        "")
    st.markdown(f"""<div><a href="https://github.com/erickfm/Dewey"><img src="{github_image_path}" style="padding-right: 10px;" width="6%" height="6%"></a>
    <a href="https://www.patreon.com/ErickFMartinez"><img src="{patreon_image_path}" style="padding-right: 10px;" width="6%" height="6%"></a></div>""",
                unsafe_allow_html=1)
