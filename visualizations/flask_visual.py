import base64
from io import BytesIO
from matplotlib.figure import Figure
from matplotlib import style, cm
import matplotlib as mpl
from pandas import Series, DataFrame
import pandas as pd
import seaborn as sns
import numpy as np

def visual_content_prod_country_flask(countries: Series):
    '''Make a bar chart for the top countries in which content is produced'''
    fig = Figure()
    ax = fig.subplots()
    g = sns.countplot(x = countries, order=countries.value_counts().index[:10], palette='dark:salmon')
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    # plt.title('Your Top 10 Content Producing Countries', fontsize=21)
    # plt.xlabel('Country', fontsize=11)
    # plt.ylabel('Titles')
    # plt.show()


    # fig = Figure()
    # ax = fig.subplots()
    # ax.plot([1, 2])
    # # Save it to a temporary buffer.
    # buf = BytesIO()
    # fig.savefig(buf, format="png")
    # # Embed the result in the html output.
    # data = base64.b64encode(buf.getbuffer()).decode("ascii")

def visual_day_activity_flask(df:DataFrame):
    '''Make a visualization to show on which days you watch netflix most.'''
    by_day = df.sort_values('Day_Name_Cat')['Day_Name_Cat'].value_counts().sort_index()
    mpl.style.use("seaborn-darkgrid")
    fig = Figure(figsize=(10,5))
    ax = fig.add_subplot(1,1,1)
    ax.set_title('Your Netflix Viewing Activity Pattern by Day', fontsize=20)
    ax.set_xlabel('Day of the week', fontsize=15)
    ax.set_ylabel('Frequency', fontsize=15)
    N = len(by_day)
    x = np.arange(N)
    colors = cm.get_cmap('viridis').reversed()
    ax.bar(by_day.index, by_day.values, color=colors(x/N))
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def visual_viewing_timeline_flask(df:DataFrame):
    by_date = pd.Series(df['Date']).value_counts().sort_index()
    by_date.index = pd.DatetimeIndex(by_date.index)
    df_date = by_date.rename_axis('Date').reset_index(name='counts')
    idx = pd.date_range(min(by_date.index), max(by_date.index))
    s = by_date.reindex(idx, fill_value=0)

    fig = Figure(figsize=(10,5))
    ax = fig.add_subplot(1,1,1)
    ax.bar(s.index, s.values)
    ax.set_title('Your Netflix Viewing Activity Timeline', fontsize=20)
    ax.set_xlabel('Date', fontsize=15)
    ax.set_ylabel('Frequency', fontsize=15)

    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def visual_top_ten_view_flask(df:DataFrame):
    """Make a bar chart visualization for the top 10 shows that you have
     watched."""
    top_views = pd.Series(df.show_title.to_list()).value_counts().nlargest(10)
    N = len(top_views)
    x = np.arange(N)
    colors = cm.get_cmap('viridis')

    fig = Figure(figsize=(10,5))
    ax = fig.add_subplot(1,1,1)
    ax.bar(top_views.index, top_views.values, color=colors(x/N))
    ax.set_title('Top 10 Shows on Netflix based on your viewing activity', fontsize=20)
    ax.set_xlabel('Show titles', fontsize=15)
    ax.set_ylabel('Frequency', fontsize=15)
    ax.set_xticks(ax.get_xticks(), top_views.index, rotation=45, ha='right', fontsize=10)
    fig.tight_layout()

    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

def visual_top_ten_timeline_flask(df:DataFrame):
    ''' Make a timeline for the top 10 shows that you have watched'''
    top_views = pd.Series(df.show_title.to_list()).value_counts().nlargest(10)
    mpl.style.use('seaborn-darkgrid')
    idx = pd.date_range(min(df['Date']), max(df['Date']))
    #plt.figure(figsize=(15,12))
    fig = Figure(figsize=(12,12))
    palette = cm.get_cmap('tab10')
    num = 0
    for title in top_views.index:
        num += 1
        ax = fig.add_subplot(6,2, num)
        #plt.subplot(6,2, num)
        ax.set_ylim(-1.0, 15)
        #plt.ylim(-1.0, 15)
        show = df[df['show_title']==title]
        showly = show['Date'].value_counts().sort_index()

        s = showly.reindex(idx, fill_value=0)
        ax.plot(s.index, s.values, marker='', color=palette(num%8), linewidth=2.5, alpha=0.9, label=title)
        ax.xaxis.set_tick_params(labelsize=8)
        ax.set_title(title, loc='left', fontsize=12, fontweight=0)
    fig.suptitle('Your top 10 viewing activity on Netflix', fontsize=20, fontweight=0, color='black', y=1.05)
    fig.tight_layout()

    #plt.show()

    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data
