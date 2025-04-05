import streamlit as st
from streamlit_option_menu import option_menu
from Home import home
from Job_open import openjob
from Job_result import resultjob
from Job_admitc import admitjob

st.set_page_config(
    page_title="Sarkari Result",
    page_icon="🧑‍🏫",
    layout="wide"
)


with st.sidebar:
    app = option_menu(
                    menu_title="Govt Job",
                    options=['Home',
                            'Latest Job',
                            'Admit Card',
                            'Results'
                            ],
                            icons=[ 'house-fill',
                            'card-text',
                            'person-vcard',
                            'journal'],
                            menu_icon="bookmark-star"
                        )
if app == 'Latest Job':
    openjob()
elif app == 'Admit Card':
     admitjob()
elif app == 'Results':
    resultjob()
elif app ==  'Home':
    home()