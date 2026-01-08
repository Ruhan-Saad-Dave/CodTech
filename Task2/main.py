import speech_recognition as sr
import gradio as gr
import numpy as np

def speech_to_text(speech):
    if speech is None:
        return "No audio recorded. Please record your voice."

    # Unpack the tuple from Gradio
    sample_rate, audio_numpy = speech

    # Convert numpy array to bytes
    audio_bytes = audio_numpy.tobytes()

    # Create an AudioData object
    audio_data = sr.AudioData(audio_bytes, sample_rate, sample_width=2)  # sample_width=2 for int16 dtype

    recognizer = sr.Recognizer()
    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Sorry, I did not get that"
    except sr.RequestError:
        return "Sorry, the service is down"

demo = gr.Interface(
    title="Speech to Text Converter",
    fn=speech_to_text,
    inputs=gr.Audio(), 
    outputs="text"
)

demo.launch()
