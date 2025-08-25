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
        # Run yt-dlp
        result = subprocess.run(
            ["yt-dlp", "-j", url],
            text=True,
            capture_output=True
        )

        if result.returncode != 0:
            return {"error": result.stderr}

        info = json.loads(result.stdout)

        return {
            "title": info.get("title"),
            "thumbnail": info.get("thumbnail"),
            "url": info.get("url"),
            "duration": info.get("duration")
        }

    except Exception as e:
        return {"error": str(e)}
