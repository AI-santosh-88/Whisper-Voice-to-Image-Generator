import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase, WebRtcMode
import openai
import numpy as np
import av
import tempfile
import os
from pydub import AudioSegment

# === MUST BE FIRST ===
st.set_page_config(page_title="Whisper Voice to Image", page_icon="🧠")

# === Background image function ===
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# === Set your background image ===
background_image_url = "https://nichefinder.xyz/upload/images/blog/what-is-ai-video.jpg?t=1706507410"
set_background(background_image_url)

# === OpenAI API Key Setup ===
openai.api_key = "api-key"

st.title(" 🧠AI 🎤Voice-to-Image Generator")
st.markdown("Speak into your mic and let Whisper transcribe it into an image prompt.")

text_output = st.empty()
image_output = st.empty()

# === Audio Processor ===
class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.frames = []

    def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
        self.frames.append(frame.to_ndarray().flatten().astype(np.int16).tobytes())
        return frame

    def get_audio(self):
        return b"".join(self.frames)

# === WebRTC Setup ===
ctx = webrtc_streamer(
    key="mic",
    mode=WebRtcMode.SENDONLY,
    audio_receiver_size=1024,
    media_stream_constraints={"audio": True, "video": False},
    audio_processor_factory=AudioProcessor,
)

# === Main App Logic ===
if ctx and ctx.audio_processor:
    if st.button("🎧 Generate Image from Voice (Whisper)"):
        audio_bytes = ctx.audio_processor.get_audio()

        if not audio_bytes:
            st.error("⚠️ No audio captured. Please try again and speak clearly.")
            st.stop()

        try:
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                wav_path = f.name

            audio_segment = AudioSegment(
                data=audio_bytes,
                sample_width=2,
                frame_rate=44100,
                channels=1
            )
            audio_segment.export(wav_path, format="wav")

            st.audio(wav_path, format="audio/wav")
            st.download_button("⬇️ Download Recorded Audio", open(wav_path, 'rb'), file_name="recorded.wav")
        except Exception as e:
            st.error(f"Audio conversion failed: {e}")
            st.stop()

        # Whisper transcription (new API format)
        try:
            with open(wav_path, "rb") as audio_file:
                transcript = openai.audio.transcriptions.create(
                    file=audio_file,
                    model="whisper-1"
                )
                prompt_text = transcript.text.strip()
                text_output.success(f"🗣️ Transcribed Prompt: **{prompt_text}**")
        except Exception as e:
            text_output.error(f"❗ Whisper transcription failed: {e}")
            st.stop()

        # Generate Image via OpenAI DALL·E
        with st.spinner("🎨 Generating image..."):
            try:
                response = openai.images.generate(
                    prompt=prompt_text,
                    n=1,
                    size="512x512"
                )
                img_url = response.data[0].url
                image_output.image(img_url, caption=prompt_text)
            except Exception as e:
                image_output.error(f"Image generation failed: {e}")
                

# Footer
st.markdown("---")
st.write("Created with ❤️ by Santosh")# Footer

