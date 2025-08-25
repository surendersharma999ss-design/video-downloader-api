import os
from fastapi import FastAPI
import subprocess
import json

app = FastAPI()

COOKIES_PATH = "cookies.txt"  # Render mounts secret files in project root

@app.get("/download")
def download_video(url: str):
    try:
        result = subprocess.run(
            ["yt-dlp", "-j", "--cookies", COOKIES_PATH, url],
            text=True,
            capture_output=True
        )

        if result.returncode != 0:
            return {"error": result.stderr.strip()}

        info = json.loads(result.stdout)
        return {
            "title": info.get("title"),
            "thumbnail": info.get("thumbnail"),
            "url": info.get("url"),
            "duration": info.get("duration")
        }

    except Exception as e:
        return {"error": str(e)}
