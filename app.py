import streamlit as st
from pages import Chat, Transcribe_Youtube

# App configuration
st.set_page_config(
    page_title='AI-VideoQA',
    page_icon='✨'
)

# Navigation
PAGES = {
    "Home" : Home,
    "Upload Video": Transcribe_Youtube,
    "Chat": Chat
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Display the selected page
page = PAGES[selection]
page.app()

