from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import os
from fastapi.responses import FileResponse
from app.services.video_analysis import understand_youtube_video

router = APIRouter()

class VideoRequest(BaseModel):
    query: str = Field(..., description="YouTube URL, video ID, or search query")
    generate_audio: bool = Field(False, description="Generate audio summary")
    analyze_sentiment: bool = Field(False, description="Include sentiment analysis")

class VideoResponse(BaseModel):
    video_title: str
    channel: str
    video_url: str
    publish_date: str
    view_count: str
    summary: str
    sentiment_analysis: Optional[str] = None
    audio_file: Optional[str] = None

@router.post("/analyze", response_model=VideoResponse)
async def analyze_video(request: VideoRequest):
    """
    Analyze YouTube video based on a search query or URL.
    Returns a summary, optional sentiment analysis, and optional audio summary.
    """
    try:
        result = understand_youtube_video(
            request.query,
            request.generate_audio,
            request.analyze_sentiment
        )
        
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
            
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/audio/{filename}")
async def get_audio(filename: str):
    """
    Get the generated audio file
    """
    # Ensure the filename is just the basename to prevent directory traversal
    base_filename = os.path.basename(filename)
    file_path = os.path.join("audio_outputs", base_filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Audio file not found")
        
    return FileResponse(file_path, media_type="audio/mpeg", filename=base_filename)