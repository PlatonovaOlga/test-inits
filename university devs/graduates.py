"""
Find and save in an excel-compatible file the top three graduates.
The function should return link to created file 
"""

from heapq import nlargest
import os
import pandas as pd

from data import gp_avg


def make_report_top3(gp_avg):
    file_name = 'report.xlsx'
    df = pd.DataFrame(nlargest(3, gp_avg, key=gp_avg.get))
    df.to_excel(file_name)
    link = os.path.abspath(os.getcwd()) + '\\' + file_name
    return link


best_graduates = make_report_top3(gp_avg)