import base64
from io import BytesIO
from matplotlib.figure import Figure
from matplotlib import style, cm
import matplotlib as mpl
from pandas import Series, DataFrame
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

def visual_day_activity(df:DataFrame):
    '''Make a visualization to show on which days you watch netflix most.'''
    by_day = df.sort_values('Day_Name_Cat')['Day_Name_Cat'].value_counts().sort_index()
    mpl.style.use("seaborn-darkgrid")
    fig = Figure(figsize=(10,5))
    #ax = fig.subplots()
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
    #plt.figure(figsize=(10,5))
    # plt.bar(by_day.index, by_day.values, color=colors(x/N))
    # plt.title('Your Netflix Viewing Activity Pattern by Day', fontsize=20)
    # plt.xlabel('Day of the week', fontsize=15)
    # plt.ylabel('Frequency', fontsize=15)
    # plt.show()