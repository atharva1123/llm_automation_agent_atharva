# app/handlers/task_b8.py
import os, speech_recognition as sr

async def handle(task_description: str) -> str:
    # For demonstration, transcribe audio from data/audio.mp3.
    input_path = os.path.abspath("data/audio.mp3")
    output_path = os.path.abspath("data/audio_transcription.txt")
    
    if not os.path.exists(input_path):
        raise Exception("Audio file not found at data/audio.mp3")
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(input_path) as source:
        audio = recognizer.record(source)
    try:
        transcription = recognizer.recognize_google(audio)
    except Exception as e:
        raise Exception("Audio transcription failed: " + str(e))
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcription)
    return "Task B8 completed: Audio transcribed and saved to data/audio_transcription.txt."
