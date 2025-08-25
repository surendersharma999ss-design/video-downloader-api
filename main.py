from fastapi import FastAPI
import subprocess
import json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Video Downloader API is running!"}

@app.get("/download")
def download_video(url: str):
    try:
        # Run yt-dlp to fetch video metadata
        result = subprocess.run(
    ["yt-dlp", "-j", "--cookies", "cookies.txt", url],
    text=True,
    capture_output=True
)
        info = json.loads(result)

        # Return a direct video URL + title
        return {
            "title": info.get("title"),
            "thumbnail": info.get("thumbnail"),
            "url": info.get("url"),
            "duration": info.get("duration")
        }
    except Exception as e:
        return {"error": str(e)}
