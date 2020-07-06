import re
import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from tabulate import tabulate
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table
import six
import datetime as dt

data = pd.read_csv('listarank.csv', delimiter=',')

now = dt.datetime.now()
current_time = now.strftime("%H:%M:%S")
data["Date"] = pd.Series([now.date()] * len(data))
data["Time"] = current_time


def render_mpl_table(data, col_width=3, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax

render_mpl_table(data, header_columns=0, col_width=3)

plt.show()
plt.savefig('listarank.png')
plt.savefig('listarank.jpeg') 