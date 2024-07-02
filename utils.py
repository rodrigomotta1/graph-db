"""
Utils functions module
"""
import sys

from config import BAR_TYPE

def update_progress(iteration:int, total:int, bar_length:int = 50):
    """
    Progress bar implementation
    """
    progress:float = iteration / total

    bar:str = BAR_TYPE['block'] * int(bar_length * progress)

    percent_progress:int = int(progress * 100)

    sys.stdout.write(f"\r[{bar:{bar_length}}] {percent_progress}%")
    sys.stdout.flush()

