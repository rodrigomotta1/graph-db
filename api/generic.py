"""
API module for scrobble csv enhancements
"""
import requests

from typing import Dict

from config import API_BASE_URL, LAST_FM_API_BASE_URL, LAST_FM_API_KEY

def _has_tags(response:dict) -> bool:
    """
    Auxiliary function to check if response has tags to be checked.
    Made to be used for track.getInfo last fm API method.
    """
    if 'track' in response:
        if 'toptags' in response['track']:
                if 'tag' in response['track']['toptags']:
                    if len(response['track']['toptags']['tag']) > 0:
                        return True
    
    return False

def get_music_info(artist:str, track:str, output_format:str = 'json') -> list[str]:
    """
    Returns a dictionary with genre, theme and style info about given artist and track

    In case of bad calls, returns a dictionary full of None values
    """

    url:str = f'{LAST_FM_API_BASE_URL}/?method=track.getInfo&artist={artist}&track={track}&api_key={LAST_FM_API_KEY}&format={output_format}'

    response:requests.Response = requests.get(url)

    if response.ok:
        data = response.json()
    
        if _has_tags(data):
            genres:list = [tag['name'] for tag in data['track']['toptags']['tag']]
            
            return genres
        else:
            return []
    else:
       print(f"\n[ERROR] Bad responses for {artist} - {track}\n")
       return []