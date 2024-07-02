"""
Constants and configurations module
"""
import os

from typing import Dict
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    load_dotenv(dotenv_file)


API_BASE_URL:str = f"https://www.theaudiodb.com/api/v1/json/2/"
"""
Used API base url. This URL is from the FreeMusicAPI hosted by theaudiodb.com (https://www.theaudiodb.com/free_music_api)

It is free with no authentication and offer calls under a limit of 2 calls per second
"""

BAR_TYPE:Dict[str, str] = {
    "block": "█"
}
"""
Progress bar style types dictionary

Currently available bar types:
    block
"""

# LAST_FM_API_BASE_URL:str | None = os.getenv("LAST_FM_API_BASE_URL")
# LAST_FM_API_KEY:str | None = os.getenv("LAST_FM_API_KEY")
# LAST_FM_SHARED_SECRET:str | None = os.getenv("LAST_FM_SHARED_SECRET")

LAST_FM_API_BASE_URL:str = "http://ws.audioscrobbler.com/2.0"
LAST_FM_API_KEY:str = "70e1a75eda93f0fdd2484b02fe7d39fa"
