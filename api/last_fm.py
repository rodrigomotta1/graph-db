"""
lastfm api interface
"""

import requests

from typing import Dict, Any

from config import LAST_FM_API_BASE_URL, LAST_FM_API_KEY


def get_music_info(artist:str, track:str, format:str = 'json'):
    """
    Search and returns music genre based on given artist and track.
    #TODO: get more information
    """
    url:str = f'{LAST_FM_API_BASE_URL}/?method=track.getInfo&artist={artist}&track={track}&api_key={LAST_FM_API_KEY}&format={format}'

    response:requests.Response = requests.get(url)

    if response.ok:
        data = response.json()

        if 'track' in data and 'name' in data['track']:
            pass

        if 'toptags' in data['track'] and 'tag' in data['track']['toptags'] and len(data['track']['toptags']['tags']) > 0:
            genres:list = [tag['name'] for tag in data['track']['toptags']['tag']]
            print(f"Genres: {', '.join(genres)}")
        else:
            print(f"No genres")
    else:
       print(f"[ERROR] Bad response for {artist} - {track}")