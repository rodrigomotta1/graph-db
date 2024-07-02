"""
Constants and configurations module
"""
from typing import Dict

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