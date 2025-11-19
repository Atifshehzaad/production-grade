import streamlit as st
import os
from openai_client import generate_questions, transcribe_audio, text_to_speech

st.set_page_config(page_title="AI Exam Generator", layout="wide")
st.title("🎓 AI Exam Preparation Generator (OpenAI Powered)")


# --------------------------
# EXAM QUESTION GENERATOR
# --------------------------
st.header("📘 Generate Questions from Text")

text_input = st.text_area("Paste course material here:", height=200)

if st.button("Generate Questions"):
    if text_input.strip():
        with st.spinner("Generating questions..."):
            result = generate_questions(text_input)
        st.success("Done!")
        st.write(result)

        # TTS Option
        if st.button("🔊 Convert Questions to Audio"):
            output_file = text_to_speech(result)
            audio_bytes = open(output_file, "rb").read()
            st.audio(audio_bytes, format="audio/mp3")

    else:
        st.warning("Please enter some text.")


# --------------------------
# SPEECH TO TEXT (WHISPER)
# --------------------------
st.header("🎤 Convert Audio to Text (Whisper STT)")

audio_file = st.file_uploader("Upload audio (mp3, wav, m4a)", type=["mp3", "wav", "m4a"])

if audio_file:
    temp_path = "uploaded_audio.tmp"
    with open(temp_path, "wb") as f:
        f.write(audio_file.read())

    if st.button("Transcribe"):
        with st.spinner("Transcribing..."):
            transcript = transcribe_audio(temp_path)
        st.success("Transcription Complete!")
        st.text_area("Transcribed Text:", transcript, height=200)


# --------------------------
# TEXT TO SPEECH
# --------------------------
st.header("🔊 Convert Text to Speech")

tts_text = st.text_area("Enter text to convert to speech:", height=120)

if st.button("Generate Audio"):
    if tts_text.strip():
        with st.spinner("Generating audio..."):
            output_file = text_to_speech(tts_text)
        st.success("Audio Ready!")
        st.audio(open(output_file, "rb").read(), format="audio/mp3")
    else:
        st.warning("Please enter text.")
