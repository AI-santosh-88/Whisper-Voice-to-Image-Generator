✅ Title :

Whisper Voice-to-Image Generator

📄 Description :

This Streamlit application captures live voice input through a microphone, transcribes the spoken words using OpenAI’s Whisper ASR model, and then generates an image based on the transcribed text using DALL·E from OpenAI. It offers an intuitive voice interface to turn speech into visual AI-generated art.

🧑‍💻 Responsibilities Covered : 

This project includes the following technical responsibilities:
1. Frontend UI Design:
* Built with Streamlit for a clean, interactive web app interface.
* Custom background using HTML/CSS styling.
2. Real-time Voice Capture:
* Implemented via streamlit-webrtc for live microphone input.
* Captures and buffers real-time audio data for processing.
3. Audio Processing & Transcription:
* Audio data converted using pydub.
* Transcription handled using OpenAI Whisper API.
4. AI-Generated Image Creation:
* Transcribed text used as a prompt to generate images via OpenAI’s DALL·E model.
5. Temporary Audio Handling:
* Uses tempfile for handling .wav files during the recording session.
* Offers download capability for recorded audio.
6. Error Handling and User Feedback:
* Ensures graceful failure and user notification during transcription or image generation failures.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📚 Libraries & Technologies Used :

Library/API - Purpose 
------------------------------------------
streamlit - Web app development & UI

streamlit-webrtc - Real-time audio input (WebRTC)

openai - Whisper transcription & DALL·E generation

numpy - Audio data handling

av - Frame processing from WebRTC

pydub - Audio conversion to WAV format

tempfile / os - Temporary file handling

📌 Summary : 

The Whisper Voice-to-Image Generator is a creative AI tool that bridges the gap between spoken language and visual art. It enables users to simply speak into a mic, see the transcribed text via OpenAI’s Whisper model, and get a matching AI-generated image from DALL·E—all within a single Streamlit app.
It showcases an engaging way to combine natural language processing, audio streaming, and generative AI in a user-friendly interface.













