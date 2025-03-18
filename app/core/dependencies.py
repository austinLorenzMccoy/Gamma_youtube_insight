from googleapiclient.discovery import build
from groq import Groq
import serpapi
import os
from app.core.config import settings

# Initialize Groq client
def get_llm_client():
    return Groq(api_key=settings.GROQ_API_KEY)

# Initialize YouTube API client
def get_youtube_client():
    return build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

# Initialize SerpAPI client
def get_serpapi_client():
    return serpapi.Client(api_key=settings.SERP_API_KEY)