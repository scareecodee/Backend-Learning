from fastapi import FastAPI, Query
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/get_download_link")
def get_download_link(insta_url: str = Query(...)):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        # Try using GET instead of POST
        res = requests.get("https://igram.world/i/", headers=headers, params={"url": insta_url})
        soup = BeautifulSoup(res.text, "html.parser")

        # Extract all links to debug
        for a in soup.find_all("a"):
            link = a.get("href")
            print("Found link:", link)

        # Look for .mp4 download links
        for a in soup.find_all("a"):
            link = a.get("href")
            if link and link.endswith(".mp4"):
                return {"download_url": link}

        return {"error": "Download link not found or not a public reel."}

    except Exception as e:
        return {"error": str(e)}
