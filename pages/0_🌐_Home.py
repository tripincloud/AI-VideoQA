import streamlit as st
from io import BytesIO


result = BytesIO()

st.set_page_config(
                   page_title='VideoQA',
                   page_icon='✨'
                )


st.header('VideoQA')

st.markdown("""
VideoQA allows you to talk with any youtube video or video you upload. Under the hood it uses the latest AI technology to transcribe the audio and then search for the answer to your question in the transcript.
            
### Features 
* **Transcribe** any youtube video or video you upload
* **Search** for any question in the video
* **Highlight** the answer in the transcript
* **Chat** LLM powered AI to answer all your questions. 

            
### How to use 
* Either upload a video or paste a youtube link
* Let the AI do the magic ask questions get answers, understand videos better. 
""")


st.markdown("""

----
### About the project & Credits
This project was developed by Tripincloud (https://github.com/tripincloud) and hosted by streamlit.
""")
