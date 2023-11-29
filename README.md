# AI-VideoQA
AI-VideoQA is a project that enables users to talk with any videos (Youtube included) and perform various NLP (Natural Language Processing) tasks.

## Functionality
The main functionality of TranscriptIQ is provided by the `transcribe_youtube.py` script. It uses the Streamlit library to create a user interface for transcribing YouTube videos and performing NLP tasks. Here is a brief overview of the functionality provided by the script:

- Retrieve YouTube video information (title, author, views, duration, etc.)
- Download YouTube videos as MP4 format
- Convert MP4 videos to MP3 audio files
- Transcribe MP3 audio files to text using speech-to-text technology
- Perform text summarization using the Cohere API
- Perform Named Entity Recognition (NER) using the Spacy library
- Generate graphs based on NER results
- Perform sentiment analysis using the VADER library
- Display word clouds based on NER results

## Usage
To use TranscriptIQ, you can run the `app.py` script. This will start the Streamlit app and you can interact with it to transcribe YouTube videos and perform NLP tasks on the transcribed text.

Note: Before running the script, make sure you have installed all the required packages listed in `requirements.txt`.

```python
streamlit run app.py
```
