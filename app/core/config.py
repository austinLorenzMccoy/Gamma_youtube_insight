import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    PROJECT_NAME: str = "YouTube Insight API"
    PROJECT_DESCRIPTION: str = "API for understanding YouTube videos without watching them"
    API_V1_STR: str = "/api/v1"
    
    # API Keys
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    YOUTUBE_API_KEY: str = os.getenv("YOUTUBE_API_KEY")
    SERP_API_KEY: str = os.getenv("SERP_API_KEY")
    
    # LLM Settings
    LLM_MODEL: str = "mixtral-8x7b-32768"
    
    # Service configuration
    AUDIO_OUTPUT_DIR: str = "audio_outputs"

settings = Settings()