## Text to Speech Translator
This project provides a web application that translates text from Spanish to English,
Italian, French, and Galician, and then generates text-to-speech audio files in these languages. 

The web interface is built using Gradio, and the text-to-speech functionality is powered by ElevenLabs.

## Install Dependencies

Install the dependencies using the following command:

```python
pip install -r requirements.txt
```
## Configure Environment Variables
Create a .env file in the root directory of the project and add your ElevenLabs API key:
```
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
```

## Usage
To run the application, use the following command:
```python
python3 main.py
```

## Documentation
[Gradio](https://www.gradio.app/)
[Elevenlabs](https://elevenlabs.io/)
[Translate](https://pypi.org/project/translate/)