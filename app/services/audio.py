import tempfile
import os
import textwrap
from gtts import gTTS
from app.core.config import settings

# Create audio output directory if it doesn't exist
os.makedirs(settings.AUDIO_OUTPUT_DIR, exist_ok=True)

def generate_speech(text, filename=None):
    """Generate speech from text using gTTS"""
    try:
        if not filename:
            # Create a temporary file for the audio
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3', dir=settings.AUDIO_OUTPUT_DIR) as temp_audio:
                filename = temp_audio.name
        
        # Use gTTS to generate audio
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        
        return filename
    except Exception as e:
        print(f"Error generating speech: {str(e)}")
        return None