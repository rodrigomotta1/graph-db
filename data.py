import pandas as pd
import os
import time

from api.generic import get_music_info
from typing import Dict, List

from tqdm import tqdm

def setup() -> None:
    """
    Pre configuration routines (?)
    """
    # Try loading environment variables from .env file
    
    # pd.set_option('display.max_columns', None)


def enhance_csv(filepath:str, output:str = "") -> None:
    """
    Include genre, theme and style information for each music in given CSV.
    # TODO: Change code to default output be None
    """
    df:pd.DataFrame = pd.read_csv(filepath).sample(n=600)

    enhanced_df = pd.DataFrame(columns=df.columns.tolist() + ['genre'])

    genres_memo:Dict[str, list] = {}

    rows:int
    cols:int
    rows, cols = df.shape
    
    iter_counter:int = 0

    for index, row in tqdm(df.iterrows(), total=len(df), desc="Enhancing CSV"):
        artist:str = row['artist']
        track:str = row['track']

        if not track in genres_memo:
            genres_memo[track] = get_music_info(artist, track)

        genres:list = genres_memo[track]

        # Debug print
        # print(f"Processing {artist} - {track} with genres: {genres}")
        
        # Skip row i`f no genre information is found
        if not genres:
            continue
        
        new_rows = []
        # Copy this row for each genre found
        for genre in genres:
            new_row = row.copy()
            new_row['genre'] = genre
            enhanced_df = pd.concat([enhanced_df, new_row.to_frame().T], ignore_index=True)
            

        # update_progress(iter_counter, rows)
        # iter_counter += 1

        # time.sleep(0.5)


    if len(output) > 0:
        enhanced_df.to_csv(output, index=False)


def show_csv_info(filepath:str, caption:str = "") -> None:
    """
    Reads csv and outputs dataframe information, like number of rows, columns and total size
    """
    rows:int
    cols:int

    df:pd.DataFrame = pd.read_csv(filepath)
    rows, cols = df.shape

    print(f"\n")

    if len(caption) > 0:
        print(f"{caption} dataframe")

    print(df.sample(5))
    print(f"\nLinhas: {rows}")
    print(f"Tam.: {os.path.getsize(filepath) / (1024 * 1024):.2f} MB")
    print(f"Colunas: {', '.join(list(df.columns))}")

    print(f"\n")


def main() -> None:
    old:str = 'scrobbles.csv' # 2024 06 28 1520
    new:str = 'enhanced.csv'

    show_csv_info(old, old)

    enhance_csv(old, new)

    show_csv_info(new, new)


if __name__ == "__main__":
    # setup()
    main()