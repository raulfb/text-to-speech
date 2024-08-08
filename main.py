import gradio as gr
from translate import Translator
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
from dotenv import dotenv_values

# Configuration .env
config = dotenv_values(".env")
ELEVENLABS_API_KEY = config["ELEVENLABS_API_KEY"]

def translator(text):
    try:
        en_transcription = Translator(
            from_lang="es", to_lang="en").translate(text)
        it_transcription = Translator(
            from_lang="es", to_lang="it").translate(text)
        fr_transcription = Translator(
            from_lang="es", to_lang="fr").translate(text)
        gl_transcription = Translator(
            from_lang="es", to_lang="gl").translate(text)
    except Exception as e:
        raise gr.Error(
            f"An error occurred while translating the text: {str(e)}")
    
    # Text to speech
    # Use Elevenlabs IO: https://elevenlabs.io/docs/api-reference/getting-started

    en_save_file_path = text_to_speach(en_transcription, "en")
    it_save_file_path = text_to_speach(it_transcription, "it")
    fr_save_file_path = text_to_speach(fr_transcription, "fr")
    ja_save_file_path = text_to_speach(gl_transcription, "gl")

    return en_save_file_path, it_save_file_path, fr_save_file_path, ja_save_file_path

def text_to_speach(text: str, language: str) -> str:

    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

        response = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",  # Adam
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=0.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        save_file_path = f"{language}.mp3"

        with open(save_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

    except Exception as e:
        raise gr.Error(
            f"An error occurred while creating the audio: {str(e)}")

    return save_file_path


web = gr.Interface(
    fn=translator,
    inputs=gr.Textbox(),
    outputs=[
        gr.Audio(label="English"),
        gr.Audio(label="Italian"),
        gr.Audio(label="French"),
        gr.Audio(label="Galician")
    ],
    title="Text to Speech",
    description="Text to speech from Spanish to English, Italian, French, and Galician"
)

web.launch()
