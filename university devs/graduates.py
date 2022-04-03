"""
Find and save in an excel-compatible file the top three graduates.
The function should return the name of the created file 
"""

from heapq import nlargest
import pandas as pd

from data import gp_avg


def make_report_top3(gp_avg):
    file_name = 'report.xlsx'
    df = pd.DataFrame(nlargest(3, gp_avg, key=gp_avg.get))
    df.to_excel(file_name)
    return file_name


best_graduates = make_report_top3(gp_avg)