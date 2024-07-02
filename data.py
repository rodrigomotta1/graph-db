import pandas as pd
import os
import time

from api.generic import get_music_info
from utils import update_progress


def setup() -> None:
    """
    Pre configuration routines (?)
    """
    pd.set_option('display.max_columns', None)


def enhance_csv(filepath:str, output:str = "") -> None:
    """
    Include genre, theme and style information for each music in given CSV.
    # TODO: Change code to default output be None
    """
    df:pd.DataFrame = pd.read_csv(filepath)
    
    # Create columns in current dataframe
    df['genre'] = None
    df['theme'] = None
    df['style'] = None

    rows:int
    cols:int
    rows, cols = df.shape
    
    iter_counter:int = 0

    for index, row in df.iterrows():
        artist:str = row['artist']
        track:str = row['track']

        music_info:dict[str, str | None] = get_music_info(artist, track)

        df.at[index, 'genre'] = music_info['genre']
        df.at[index, 'theme'] = music_info['theme']
        df.at[index, 'style'] = music_info['style']

        update_progress(iter_counter, rows)
        iter_counter += 1

        time.sleep(0.5)

    if len(output) > 0:
        df.to_csv(output, index=False)


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