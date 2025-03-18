from youtube_transcript_api import YouTubeTranscriptApi

def extract_youtube_transcript(video_id):
    """Extract transcript from a YouTube video"""
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([item['text'] for item in transcript_list])
        return transcript_text
    except Exception as e:
        print(f"Error extracting transcript: {str(e)}")
        return None