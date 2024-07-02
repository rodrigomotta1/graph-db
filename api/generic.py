"""
API module for scrobble csv enhancements
"""
import requests

from typing import Dict

from config import API_BASE_URL


def get_music_info(artist:str, track:str) -> Dict[str, str | None]:
    """
    Returns a dictionary with genre, theme and style info about given artist and track

    In case of bad calls, returns a dictionary full of None values
    """
    url:str = f"{API_BASE_URL}/searchtrack.php?s={artist}&t={track}"

    response = requests.get(url)

    if response.ok:
        data = response.json()

        if data and 'track' in data and data['track']:
            track_info = data['track'][0]

            return {
                'genre': track_info.get("strGenre"),
                'theme': track_info.get("strTheme"),
                'style': track_info.get("strStyle"),                    
            }
        
    else:
        print(f"[WARNING] Bad response at get_music_info: {response.content}")

    return {
        'genre': None,
        'theme': None,
        'style': None,                    
    }