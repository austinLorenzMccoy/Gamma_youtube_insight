import re
from app.core.dependencies import get_youtube_client

# Get YouTube client
youtube = get_youtube_client()

def search_youtube_video(query):
    """Search for YouTube videos based on the query"""
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=5
    )
    response = request.execute()
    
    # Return the top result
    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        video_title = response['items'][0]['snippet']['title']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return {
            "video_id": video_id,
            "title": video_title,
            "url": video_url
        }
    else:
        return None

def get_video_details(video_id):
    """Get additional details about a YouTube video"""
    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=video_id
    )
    response = request.execute()
    
    if response['items']:
        video_info = response['items'][0]
        return {
            "title": video_info['snippet']['title'],
            "description": video_info['snippet']['description'],
            "channel": video_info['snippet']['channelTitle'],
            "publish_date": video_info['snippet']['publishedAt'],
            "view_count": video_info['statistics'].get('viewCount', 'N/A'),
            "like_count": video_info['statistics'].get('likeCount', 'N/A'),
            "comment_count": video_info['statistics'].get('commentCount', 'N/A'),
            "duration": video_info['contentDetails']['duration']
        }
    else:
        return None

def extract_video_id_from_url(url):
    """Extract video ID from YouTube URL"""
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None