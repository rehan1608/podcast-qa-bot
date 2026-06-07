import whisper
import json

def transcribe_audio(audio_path):
    print("Loading Whisper model (this might take a few minutes)...")
    # Using 'base' for a balance of speed and accuracy
    model = whisper.load_model("base") 
    
    print("Transcribing audio with timestamps...")
    result = model.transcribe(audio_path, verbose=False)
    
    # Save the detailed segments (which include 'start' and 'end' times)
    with open("transcript_segments.json", "w", encoding="utf-8") as f:
        json.dump(result["segments"], f, indent=4, ensure_ascii=False)
        
    print("Transcription saved to transcript_segments.json!")

if __name__ == "__main__":
    transcribe_audio("podcast_audio.mp3")