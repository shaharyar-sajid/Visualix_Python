from typing import Tuple, Union
import pandas as pd
#import imdb
#from tqdm import tqdm

def load_csv_file(path:str) -> Union[pd.DataFrame,None]:
    '''Loads the csv file using pandas.read_csv and sets the parse_date
     attribute to Date and dayfirst to True.
     path: Pass the path to the CSV file
     
     Returns: A pandas.DataFrame is returned if successful else None is
     returned'''

    if path.lower().endswith('.csv'):
        df = pd.read_csv(path, parse_dates=['Date'], dayfirst=True)
        return df

    else:
        print('CSV not found')
        return None

def load_stream_file(stream) -> Union[pd.DataFrame,None]:
    '''Loads the csv file from the buffer stream using pandas.read_csv and sets the parse_date
     attribute to Date and dayfirst to True.
     path: Pass the path to the CSV file
     
     Returns: Return a pandas DataFrame'''

    df = pd.read_csv(stream, parse_dates=['Date'], dayfirst=True)
    return df

def split_title(df:pd.DataFrame):
    '''Splits the Title column of dataframe based on ":" into
     3 columns. These columns are show_title, season and episode_name.
     It also creates the show_type columns and sets its value depenging
      on the value in season column'''

    show_details = df.Title.str.split(":",expand=True,n=2)
    df['show_title'] = show_details[0]
    df['season'] = show_details[1]
    df['episode_name'] = show_details[2]
    df['show_type'] = df.apply(lambda x:'Movie' if pd.isnull(x['season']) else 'TV Show' , axis=1)

def split_date(df:pd.DataFrame):
    '''Split the Date column into Day_name, Year, Month and Day Column'''
    df['Day_Name'] = df.Date.dt.day_name()
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month_name()
    df['Day'] = df['Date'].dt.day

def make_genre_column(df:pd.DataFrame, genres:list):
    '''Create a genres column in the dataframe that is passed as input'''
    titles = df['show_title'].unique()
    movie_genre_dict = dict(zip(titles,genres))
    df['genre'] = [','.join(movie_genre_dict[st]) if movie_genre_dict.get(st) is not None else None for st in df['show_title']]    

def get_imdb_genre_and_country(df:pd.DataFrame) -> Tuple[list, pd.DataFrame]:
    '''Uses the Cinemagoer package to retrive genre and the countriees in
     the content is produced about movies and tv show'''

    ia = imdb.Cinemagoer()
    titles = df['show_title'].unique()
    movie_ids = [ia.search_movie(mov, results=1)[0].movieID for mov in tqdm(titles, desc='Searching for movies')]
    movies_info = [ia.get_movie(x, info=['main']) for x in tqdm(movie_ids, desc='Retrieving information')]
    genres = [x.get('genre') for x in movies_info]
    movie_countries = [','.join(x.get('countries')) if x.get('countries') is not None else 'production country unavailable' for x in movies_info]
    movie_countries = pd.DataFrame(movie_countries, columns=['production_country'])
    return genres,movie_countries

def get_country_list(movie_countries:pd.DataFrame) -> pd.Series:
    countries = movie_countries.production_country.str.split(',', expand=True).stack().reset_index(level=1, drop=True);
    countries = countries[countries != 'production country unavailable']
    return countries

def make_day_categorical(df:pd.DataFrame):
    '''Make a categorical column for days of week'''

    dayNames = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['Day_Name_Cat'] = pd.Categorical(df['Day_Name'], categories=dayNames, ordered=True)