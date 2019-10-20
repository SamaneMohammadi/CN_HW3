from pandas import DataFrame
import pandas as pd
import os


def get_file_name( path):
    return os.path.basename(path).split(".")[0].strip().lower()


name = get_file_name('C:/Users/gunash/Downloads/data.txt')
with open('C:/Users/gunash/Downloads/data.txt') as f:
    df = DataFrame(0.0, index=[1,2,3], columns=[1,2,3])
    for line in f:
        data = line.strip().split()
        row,column,value = [int(i) if i.isdigit() else float(i) for i in data]
        df.set_value(row,column,value)
m[name] = df