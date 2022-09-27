from matplotlib import blocking_input
from pandas import DataFrame, Series
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from plotly.offline import plot
import plotly.graph_objects as go

def visual_content_prod_country(countries: Series):
    '''Make a bar chart for the top countries in which content is produced'''
    plt.figure(figsize=(15,8))
    g = sns.countplot(x = countries, order=countries.value_counts().index[:10], palette='dark:salmon')
    plt.title('Your Top 10 Content Producing Countries', fontsize=21)
    plt.xlabel('Country', fontsize=11)
    plt.ylabel('Titles')
    plt.show()

def visual_map_prod_country(countries: Series):
    '''Make a map visulization to hightlight the countries from which you
    have watched content'''
    plot([go.Choropleth(
    locationmode='country names',
    locations=countries.value_counts().keys(),
    z=countries.value_counts().values,
    colorscale = 'Rainbow',
    )])

def visual_top_ten_view(df:DataFrame):
    """Make a bar chart visualization for the top 10 shows that you have
     watched."""
    top_views = pd.Series(df.show_title.to_list()).value_counts().nlargest(10)
    N = len(top_views)
    x = np.arange(N)
    colors = plt.get_cmap('viridis')

    plt.figure(figsize=(10,5))
    plt.bar(top_views.index, top_views.values, color=colors(x/N))
    plt.ylabel("Frequency", fontsize=12)
    plt.xlabel("Show titles", fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=11)
    plt.title("Top 10 Shows on Netflix based on your viewing activity", fontsize=16)
    plt.show()

def visual_top_ten_genre(df:DataFrame):
    '''Make a visualization for the top ten genres watched.'''

    top_genres = df.set_index('show_title').genre.str.split(',', expand=True).stack().reset_index(level=1, drop=True)
    plt.figure(figsize=(10, 10))
    sns.countplot(y=top_genres, order=top_genres.value_counts().index.to_list()[:10], palette='Greens_r', saturation=.4)
    plt.title('Your Top 10 most watched genres', fontsize=21);
    plt.show()

def visual_day_activity(df:DataFrame):
    '''Make a visualization to show on which days you watch netflix most.'''
    by_day = df.sort_values('Day_Name_Cat')['Day_Name_Cat'].value_counts().sort_index()
    plt.style.use("seaborn-darkgrid")
    N = len(by_day)
    x = np.arange(N)
    colors = plt.get_cmap('viridis').reversed()

    plt.figure(figsize=(10,5))
    plt.bar(by_day.index, by_day.values, color=colors(x/N))
    plt.title('Your Netflix Viewing Activity Pattern by Day', fontsize=20)
    plt.xlabel('Day of the week', fontsize=15)
    plt.ylabel('Frequency', fontsize=15)
    plt.show()

def visual_viewing_timeline(df:DataFrame):
    by_date = pd.Series(df['Date']).value_counts().sort_index()
    by_date.index = pd.DatetimeIndex(by_date.index)
    df_date = by_date.rename_axis('Date').reset_index(name='counts')

    idx = pd.date_range(min(by_date.index), max(by_date.index))
    s = by_date.reindex(idx, fill_value=0)
    plt.figure(figsize=(20,8))
    plt.bar(s.index, s.values)
    plt.title("Your Netflix Viewing Activity Timeline", fontsize=20)
    plt.xlabel("Date", fontsize=15)
    plt.ylabel("Frequency", fontsize=15)
    plt.show()

def visual_top_ten_timeline(df:DataFrame):
    ''' Make a timeline for the top 10 shows that you have watched'''
    top_views = pd.Series(df.show_title.to_list()).value_counts().nlargest(10)
    plt.style.use('seaborn-darkgrid')
    idx = pd.date_range(min(df['Date']), max(df['Date']))
    plt.figure(figsize=(15,12))
    palette = plt.get_cmap('tab10')
    num = 0
    for title in top_views.index:
        num += 1
        plt.subplot(6,2, num)
        plt.ylim(-1.0, 15)
        show = df[df['show_title']==title]
        showly = show['Date'].value_counts().sort_index()

        s = showly.reindex(idx, fill_value=0)
        plt.plot(s.index, s.values, marker='', color=palette(num%8), linewidth=2.5, alpha=0.9, label=title)

        plt.title(title, loc='left', fontsize=12, fontweight=0)
    plt.suptitle('Your top 10 viewing activity on Netflix', fontsize=20, fontweight=0, color='black', y=1.05)
    plt.tight_layout()

    plt.show()