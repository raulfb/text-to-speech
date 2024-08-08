import gradio as gr
from translate import Translator

def translator(text):
    
    try:
        en_transcription = Translator(
            from_lang="es", to_lang="en").translate(text)
        it_transcription = Translator(
            from_lang="es", to_lang="it").translate(text)
        fr_transcription = Translator(
            from_lang="es", to_lang="fr").translate(text)
        ja_transcription = Translator(
            from_lang="es", to_lang="ja").translate(text)
    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error traduciendo el texto: {str(e)}")

    print(f"Texto traducido a Inglés: {en_transcription}")
    print(f"Texto traducido a Italiano: {it_transcription}")
    print(f"Texto traducido a Francés: {fr_transcription}")
    print(f"Texto traducido a Japonés: {ja_transcription}")



web = gr.Interface(
    fn=translator,
    inputs=gr.Textbox(
        # sources=["microphone"],
        # type="filepath",
        # label="Español"
    ),
    outputs=[
        gr.Audio(label="Inglés"),
        gr.Audio(label="Italiano"),
        gr.Audio(label="Francés"),
        gr.Audio(label="Japonés")
    ],
    title="Traductor de voz",
    description="Traductor de voz con IA a varios idiomas"
)

web.launch()

print("hello world")