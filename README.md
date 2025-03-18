# 🎬 Gamma YouTube Insight

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg)](https://fastapi.tiangolo.com)
[![Groq](https://img.shields.io/badge/Groq-Powered-6366F1.svg)](https://groq.com)

![Gamma YouTube Insight Banner](https://raw.githubusercontent.com/austinLorenzMccoy/Gamma_youtube_insight/main/assets/banner.png)

## 📋 Overview

**Gamma YouTube Insight** is a sophisticated API service that transforms how we consume YouTube content. Don't have time to watch that 45-minute educational video? Need key takeaways from a lengthy product review? Gamma YouTube Insight has you covered!

This service leverages the power of Large Language Models (LLMs) via Groq to provide comprehensive summaries, sentiment analysis, and even audio narration of YouTube videos based solely on their transcripts. Experience the content without the time investment.

## ✨ Features

- 🔍 **Smart Search**: Find videos with just a search query or analyze specific videos via URL
- 📝 **Comprehensive Summaries**: Get detailed summaries that capture the essence of any video
- 🔊 **Audio Narration**: Convert summaries to speech for on-the-go consumption
- 💭 **Sentiment Analysis**: Understand the emotional tone and key sentiments expressed
- ⚡ **Lightning Fast**: Powered by Groq's high-performance inference API
- 🌐 **RESTful API**: Easy integration with existing applications

## 🚀 Installation

### Prerequisites

- Python 3.8+
- API keys for:
  - [Groq](https://console.groq.com)
  - [YouTube Data API](https://developers.google.com/youtube/v3/getting-started)
  - [SerpAPI](https://serpapi.com) (for web search capabilities)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/austinLorenzMccoy/Gamma_youtube_insight.git
   cd Gamma_youtube_insight
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables by creating a `.env` file:
   ```
   GROQ_API_KEY=your_groq_api_key
   YOUTUBE_API_KEY=your_youtube_api_key
   SERP_API_KEY=your_serpapi_key
   ```

5. Launch the application:
   ```bash
   python main.py
   ```

6. Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs)

## 📚 API Usage

### Analyze a YouTube Video

```python
import requests

response = requests.post(
    "http://localhost:8000/api/v1/analyze",
    json={
        "query": "How to learn FastAPI in 10 minutes",  # Search query or YouTube URL
        "generate_audio": True,
        "analyze_sentiment": True
    }
)

result = response.json()
print(f"Video: {result['video_title']}")
print(f"Summary: {result['summary'][:150]}...")

# If audio was generated
if "audio_file" in result:
    print(f"Audio summary available at: {result['audio_file']}")
```

### Using cURL

```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/analyze' \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "generate_audio": true,
    "analyze_sentiment": true
  }'
```

## 🧩 Project Structure

```
youtube_insight/
├── .env                    # Environment variables
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Project dependencies
└── app/
    ├── __init__.py
    ├── api/
    │   ├── __init__.py
    │   └── routes.py       # API routes/endpoints
    ├── core/
    │   ├── __init__.py
    │   ├── config.py       # Configuration settings
    │   └── dependencies.py # Dependencies and service initialization
    └── services/
        ├── __init__.py
        ├── youtube.py      # YouTube API related functions
        ├── transcript.py   # Transcript extraction and processing
        ├── llm.py          # LLM integration for summarization
        ├── search.py       # Web search functionality
        ├── audio.py        # Audio generation functionality
        └── video_analysis.py # Main video analysis service
```

## 💡 Use Cases

- **Education**: Quickly grasp the main concepts from educational content
- **Research**: Efficiently process multiple video sources for research
- **Content Creation**: Analyze competitor videos or gather insights on trends
- **Accessibility**: Make video content accessible to those with hearing impairments
- **Productivity**: Stay informed while focusing on other tasks using audio summaries

## 🧠 How It Works

1. **Video Identification**: The system either searches for a video based on your query or processes a direct YouTube URL
2. **Transcript Extraction**: Using the YouTube Transcript API, the system extracts available captions
3. **Content Analysis**: The transcript is processed by Groq's Mixtral model to generate a comprehensive summary
4. **Sentiment Analysis**: (Optional) The system evaluates the emotional tone and key sentiments
5. **Audio Generation**: (Optional) The summary is converted to speech using gTTS
6. **Results Delivery**: All insights are packaged and returned via the API

## 🛠️ Technologies Used

- **FastAPI**: High-performance web framework
- **Groq**: LLM inference API for content summarization and analysis
- **YouTube Data API**: For video metadata and search capabilities
- **YouTube Transcript API**: For extracting video transcripts
- **gTTS (Google Text-to-Speech)**: For audio generation
- **SerpAPI**: For web search capabilities

## 📊 Performance

The service is designed for efficiency, with most video analyses completing in under 10 seconds (depending on transcript length). Audio generation may add a few additional seconds to the processing time.

## 🔒 Security Notes

- The application does not store or retain video content
- API keys should be kept secure and never exposed in client-side code
- Consider implementing rate limiting for production deployments

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🙏 Acknowledgements

- [Groq](https://groq.com) for providing high-speed inference capabilities
- [YouTube Data API](https://developers.google.com/youtube/v3) for video metadata access
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction
- [FastAPI](https://fastapi.tiangolo.com) for the elegant web framework

## 📞 Contact

Austin Lorenz McCoy - [@austinLorenzMccoy](https://github.com/austinLorenzMccoy)

Project Link: [https://github.com/austinLorenzMccoy/Gamma_youtube_insight](https://github.com/austinLorenzMccoy/Gamma_youtube_insight)

---

<p align="center">
  <i>Made with ❤️ for YouTube content consumers everywhere</i>
</p>