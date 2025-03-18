from app.core.dependencies import get_llm_client
from app.core.config import settings

# Get LLM client
client = get_llm_client()

def summarize_video_content(transcript, video_details):
    """Generate a summary of the video content using the LLM"""
    # Create a prompt for the LLM to summarize the video
    prompt = f"""
    Video Title: {video_details['title']}
    Channel: {video_details['channel']}
    
    Create a comprehensive summary of this video based on the transcript below.
    Include:
    1. A brief but detailed summary of the main content
    2. Key themes or points discussed
    3. Important characters or people mentioned
    4. The overall tone and sentiment of the video
    5. Any significant plot twists or revelations (if applicable)
    
    Make the summary feel like the person has actually watched the video.
    
    Transcript:
    {transcript[:8000]}  # Limit transcript length to avoid token limits
    """
    
    # Call the LLM API to generate the summary
    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are an expert video content analyzer. Your task is to provide comprehensive summaries of videos based on their transcripts."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000
    )
    
    return response.choices[0].message.content

def analyze_sentiment(transcript):
    """Analyze sentiment of the video content"""
    prompt = f"""
    Analyze the sentiment and emotional tone of the following video transcript.
    Provide:
    1. Overall sentiment (positive, negative, neutral, mixed)
    2. Key emotions expressed
    3. Any noticeable shifts in tone
    
    Transcript:
    {transcript[:5000]}  # Limit transcript length
    """
    
    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=[
            {"role": "system", "content": "You are an expert in sentiment analysis."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    return response.choices[0].message.content