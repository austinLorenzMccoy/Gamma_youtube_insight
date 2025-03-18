import textwrap
from app.services.youtube import search_youtube_video, get_video_details, extract_video_id_from_url
from app.services.transcript import extract_youtube_transcript
from app.services.llm import summarize_video_content, analyze_sentiment
from app.services.audio import generate_speech

def understand_youtube_video(input_query, generate_audio=False, analyze_sentiment_flag=False):
    """Main function to understand YouTube videos without watching them"""
    # Step 1: Determine if input is a URL or a search query
    if "youtube.com" in input_query or "youtu.be" in input_query:
        video_id = extract_video_id_from_url(input_query)
        if not video_id:
            return {"error": "Invalid YouTube URL"}
        
        video_details = get_video_details(video_id)
        if not video_details:
            return {"error": "Could not fetch video details"}
        
        video_url = f"https://www.youtube.com/watch?v={video_id}"
    else:
        # Search for the video
        search_result = search_youtube_video(input_query)
        if not search_result:
            return {"error": "No videos found matching your query"}
        
        video_id = search_result["video_id"]
        video_url = search_result["url"]
        video_details = get_video_details(video_id)
    
    # Step 2: Extract transcript
    transcript = extract_youtube_transcript(video_id)
    if not transcript:
        return {
            "error": "Could not extract transcript. This might be due to unavailable captions or restricted content.",
            "video_url": video_url,
            "video_details": video_details
        }
    
    # Step 3: Generate summary
    summary = summarize_video_content(transcript, video_details)
    
    # Step 4: Additional analysis (if requested)
    sentiment_analysis = None
    if analyze_sentiment_flag:
        sentiment_analysis = analyze_sentiment(transcript)
    
    # Step 5: Generate audio (if requested)
    audio_file = None
    if generate_audio:
        # Use a shorter version of the summary for audio
        audio_summary = textwrap.shorten(summary, width=2000, placeholder="...")
        audio_file = generate_speech(audio_summary)
    
    # Step 6: Prepare and return the results
    result = {
        "video_title": video_details["title"],
        "channel": video_details["channel"],
        "video_url": video_url,
        "publish_date": video_details["publish_date"],
        "view_count": video_details["view_count"],
        "summary": summary
    }
    
    if sentiment_analysis:
        result["sentiment_analysis"] = sentiment_analysis
    
    if audio_file:
        result["audio_file"] = audio_file
    
    return result