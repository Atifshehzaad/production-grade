import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


# --- GPT Text Generation ---
def generate_questions(text):
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You create high-quality exam questions."},
            {"role": "user", "content": f"Generate 10 exam questions from:\n\n{text}"}
        ],
        temperature=0.6
    )
    return response.choices[0].message["content"]


# --- Whisper Speech to Text ---
def transcribe_audio(file_path):
    with open(file_path, "rb") as audio:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio
        )
    return transcript.text


# --- Text to Speech (OpenAI TTS) ---
def text_to_speech(text, output="tts_output.mp3"):
    response = openai.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )
    audio_bytes = response.read()
    with open(output, "wb") as f:
        f.write(audio_bytes)
    return output
